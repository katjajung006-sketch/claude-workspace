#!/usr/bin/env python3
"""Täglicher Instagram-Späher für yoga.statt.funktionieren.

Holt von den konfigurierten Accounts die neuesten Beiträge (über Apify),
erkennt neue Reels/Posts seit dem letzten Lauf, lässt sie – falls das
Claude Code CLI installiert ist – durch Katjas Strategie/Marke analysieren
und schickt das Ergebnis per Telegram.

Nur Python-Standardbibliothek, keine pip-Pakete nötig.
"""

import json
import os
import shutil
import subprocess
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent.parent
CONFIG_PATH = HERE / "config.json"
STATE_PATH = HERE / "state.json"

APIFY_ACTOR = "apify~instagram-scraper"
TELEGRAM_LIMIT = 4096

# Vorübergehende Netzwerk-Aussetzer (Connection reset, Timeout) abfangen:
# scheitert ein Abruf, wird er mit wachsender Pause erneut versucht.
FETCH_RETRIES = 3
FETCH_BACKOFF = (5, 15, 30)  # Sekunden Pause vor Versuch 2, 3, …


# ---------- Hilfen ----------

def log(msg):
    print(f"[{datetime.now().isoformat(timespec='seconds')}] {msg}", flush=True)


def load_json(path, default):
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def save_json(path, data):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(path)


def read_context_file(rel_path, max_chars):
    p = WORKSPACE / rel_path
    if not p.exists():
        return ""
    text = p.read_text(encoding="utf-8")
    return text[:max_chars]


# ---------- Instagram über Apify ----------

def _apify_fetch_once(token, account_url, limit):
    url = (
        f"https://api.apify.com/v2/acts/{APIFY_ACTOR}"
        f"/run-sync-get-dataset-items?token={token}"
    )
    payload = {
        "directUrls": [account_url],
        "resultsType": "posts",
        "resultsLimit": limit,
        "addParentData": False,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.load(resp)


def apify_fetch(token, account_url, limit):
    """Abruf mit automatischen Wiederholungen bei vorübergehenden Aussetzern.

    Fängt Connection-Resets/Timeouts ab, die einzelne Läufe sonst killen.
    HTTP-Fehler ab 400 (z. B. falscher Token, Account gesperrt) sind dauerhaft
    und werden nicht wiederholt.
    """
    last_err = None
    for attempt in range(1, FETCH_RETRIES + 1):
        try:
            return _apify_fetch_once(token, account_url, limit)
        except urllib.error.HTTPError as e:
            # 429/5xx sind oft vorübergehend → erneut versuchen; 4xx sonst nicht.
            if e.code != 429 and 400 <= e.code < 500:
                raise
            last_err = e
        except Exception as e:
            last_err = e
        if attempt < FETCH_RETRIES:
            pause = FETCH_BACKOFF[min(attempt - 1, len(FETCH_BACKOFF) - 1)]
            log(f"  Abruf-Versuch {attempt} scheiterte ({type(last_err).__name__}), "
                f"erneuter Versuch in {pause}s")
            time.sleep(pause)
    raise last_err


def is_reel(post):
    return post.get("type") == "Video" or post.get("productType") == "clips"


def post_kind(post):
    if is_reel(post):
        return "Reel/Video"
    if post.get("type") == "Sidecar":
        return "Carousel"
    return "Bild"


def normalise(post):
    return {
        "shortcode": post.get("shortCode") or post.get("shortcode") or post.get("id"),
        "kind": post_kind(post),
        "caption": (post.get("caption") or "").strip(),
        "url": post.get("url") or "",
        "timestamp": post.get("timestamp") or "",
        "likes": post.get("likesCount"),
        "comments": post.get("commentsCount"),
        "views": post.get("videoViewCount"),
    }


# ---------- Telegram ----------

def telegram_send(token, chat_id, text):
    for i in range(0, len(text), TELEGRAM_LIMIT):
        chunk = text[i:i + TELEGRAM_LIMIT]
        payload = json.dumps({
            "chat_id": chat_id,
            "text": chunk,
            "disable_web_page_preview": False,
        }).encode("utf-8")
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        try:
            urllib.request.urlopen(req, timeout=30).read()
        except urllib.error.HTTPError as e:
            log(f"Telegram-Fehler: {e.code} {e.read().decode('utf-8', 'ignore')[:300]}")
            raise


# ---------- Analyse über Claude Code CLI (falls vorhanden) ----------

def find_claude():
    for name in ("claude",):
        p = shutil.which(name)
        if p:
            return p
    for cand in (
        "/opt/homebrew/bin/claude",
        "/usr/local/bin/claude",
        str(Path.home() / ".local/bin/claude"),
    ):
        if Path(cand).exists():
            return cand
    return None


def build_analysis_prompt(new_by_account):
    brand = read_context_file("context/brand-voice.md", 3500)
    soul = read_context_file("context/soulclient.md", 3500)
    rivals = read_context_file("reference/wettbewerber-instagram.md", 4000)

    blocks = []
    for username, posts in new_by_account.items():
        lines = [f"### Account: @{username}"]
        for p in posts:
            metric = []
            if p["likes"] is not None:
                metric.append(f"{p['likes']} Likes")
            if p["views"] is not None:
                metric.append(f"{p['views']} Views")
            if p["comments"] is not None:
                metric.append(f"{p['comments']} Kommentare")
            lines.append(
                f"- [{p['kind']}] {p['url']}\n"
                f"  Datum: {p['timestamp']} | {', '.join(metric) or 'keine Zahlen'}\n"
                f"  Caption: {p['caption'][:600]}"
            )
        blocks.append("\n".join(lines))
    posts_text = "\n\n".join(blocks)

    return f"""Du bist Katjas Content-Stratege. Katja macht Instagram-Content unter \
@yoga.statt.funktionieren: ruhiges Yoga + Nervensystem-/Funktionsmodus-Sprache für \
Frauen 40+. Unten stehen NEUE Beiträge ihrer drei wichtigsten Wettbewerber seit gestern.

Analysiere jeden Beitrag kurz und konkret. Pro Beitrag:
- Erste Zeile: Accountname + kurze Einordnung.
- Zweite Zeile: die exakte Beitrags-URL mit einem 🔗 davor. Kopiere die URL Zeichen \
für Zeichen aus den Beitragsdaten unten — niemals erfinden, kürzen oder ändern.
- Was ist es (Format, Hook-Mechanik)?
- Warum funktioniert es – oder warum nicht?
- Was nimmt Katja konkret für ihren eigenen Content mit (1 umsetzbarer Satz)?

Danach ein kurzer Block "Heute auffällig": Muster, das über die Accounts hinweg sichtbar wird.

REGELN für deinen Text:
- Schreib wie ein Mensch, kein KI-Klang. Keine Floskeln, kein "Hier ist", kein \
"Zusammenfassend", kein gleichförmiger Rhythmus.
- Knapp und brauchbar. Telegram-Nachricht, kein Essay.
- KEINE Markdown-Zeichen: keine Sternchen (* oder **), keine Rauten (#). Reiner Text.
  Für eine Überschrift einfach eine eigene Zeile, für Betonung notfalls GROSSBUCHSTABEN.
  (Ausnahme: das 🔗 vor der URL ist erwünscht.)
- Auf Deutsch.

--- KONTEXT: KATJAS MARKENSTIMME ---
{brand}

--- KONTEXT: ZIELGRUPPE (Soulclient) ---
{soul}

--- KONTEXT: WAS BEI WELCHEM WETTBEWERBER ZU LERNEN IST ---
{rivals}

--- NEUE BEITRÄGE HEUTE ---
{posts_text}
"""


def run_analysis(claude_bin, prompt):
    try:
        result = subprocess.run(
            [claude_bin, "-p"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=420,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        log(f"Claude CLI Rückgabe {result.returncode}: {result.stderr[:300]}")
    except Exception as e:
        log(f"Claude CLI Fehler: {type(e).__name__} {e}")
    return None


# ---------- einfache Benachrichtigung (Fallback ohne CLI) ----------

def build_plain_digest(new_by_account):
    out = ["Neue Beiträge bei deinen 3 Wettbewerbern:\n"]
    for username, posts in new_by_account.items():
        out.append(f"@{username}")
        for p in posts:
            metric = []
            if p["likes"] is not None:
                metric.append(f"{p['likes']} Likes")
            if p["views"] is not None:
                metric.append(f"{p['views']} Views")
            cap = p["caption"].replace("\n", " ")[:160]
            out.append(f"  • [{p['kind']}] {' · '.join(metric)}\n    {cap}\n    {p['url']}")
        out.append("")
    return "\n".join(out)


# ---------- Hauptlauf ----------

def main():
    if not CONFIG_PATH.exists():
        log("config.json fehlt. Bitte config.example.json kopieren und ausfüllen.")
        sys.exit(1)

    cfg = load_json(CONFIG_PATH, {})
    apify_token = cfg.get("apify_token", "").strip()
    tg_token = cfg.get("telegram_bot_token", "").strip()
    tg_chat = str(cfg.get("telegram_chat_id", "")).strip()
    accounts = cfg.get("accounts", [])
    per_account = int(cfg.get("posts_per_account", 6))

    missing = [k for k, v in {
        "apify_token": apify_token,
        "telegram_bot_token": tg_token,
        "telegram_chat_id": tg_chat,
    }.items() if not v or v.startswith("HIER_")]
    if missing:
        log(f"Bitte in config.json eintragen: {', '.join(missing)}")
        sys.exit(1)

    state = load_json(STATE_PATH, {})
    new_by_account = {}
    baseline_accounts = []
    errors = []

    for acc in accounts:
        username = acc["username"]
        url = acc["url"]
        try:
            raw = apify_fetch(apify_token, url, per_account)
        except Exception as e:
            errors.append(f"@{username}: {type(e).__name__} {str(e)[:160]}")
            log(f"Abruf fehlgeschlagen @{username}: {e}")
            continue

        posts = [normalise(p) for p in raw if (p.get("shortCode") or p.get("id"))]
        current_codes = [p["shortcode"] for p in posts]
        seen = set(state.get(username, []))

        if username not in state:
            # Erster Lauf: aktuellen Stand merken, NICHTS melden (kein Flut-Report).
            state[username] = current_codes
            baseline_accounts.append((username, len(current_codes)))
            continue

        fresh = [p for p in posts if p["shortcode"] not in seen]
        if fresh:
            new_by_account[username] = fresh
        # Stand aktualisieren (alte + neue, begrenzt)
        state[username] = list(dict.fromkeys(current_codes + list(seen)))[:60]

    save_json(STATE_PATH, state)

    # --- Nachricht zusammenbauen & senden ---
    date_str = datetime.now().strftime("%d.%m.%Y")

    if baseline_accounts:
        lines = [f"Instagram-Späher eingerichtet ({date_str}).",
                 "Aktueller Stand gespeichert – ab morgen melde ich neue Beiträge:"]
        for u, n in baseline_accounts:
            lines.append(f"  • @{u}: {n} Beiträge erfasst")
        if errors:
            lines.append("\nProbleme beim Abruf:")
            lines += [f"  • {e}" for e in errors]
        telegram_send(tg_token, tg_chat, "\n".join(lines))
        log("Baseline gesetzt.")
        return

    if not new_by_account:
        msg = f"Instagram-Späher {date_str}: heute nichts Neues bei deinen 3 Accounts."
        if errors:
            msg += "\n\nProbleme beim Abruf:\n" + "\n".join(f"  • {e}" for e in errors)
        telegram_send(tg_token, tg_chat, msg)
        log("Keine neuen Beiträge.")
        return

    count = sum(len(v) for v in new_by_account.values())
    header = f"☀️ Instagram-Späher {date_str} — {count} neue(r) Beitrag/Beiträge\n"

    claude_bin = find_claude()
    body = None
    if claude_bin:
        log(f"Analyse via Claude CLI: {claude_bin}")
        body = run_analysis(claude_bin, build_analysis_prompt(new_by_account))
    if not body:
        log("Keine CLI-Analyse — sende einfache Benachrichtigung.")
        body = build_plain_digest(new_by_account)

    full = header + "\n" + body
    if errors:
        full += "\n\nProbleme beim Abruf:\n" + "\n".join(f"  • {e}" for e in errors)
    telegram_send(tg_token, tg_chat, full)
    log(f"Gesendet: {count} neue Beiträge.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log(f"FATAL: {type(e).__name__} {e}")
        # Versuch, den Fehler auch per Telegram zu melden
        try:
            cfg = load_json(CONFIG_PATH, {})
            telegram_send(
                cfg.get("telegram_bot_token", ""),
                str(cfg.get("telegram_chat_id", "")),
                f"⚠️ Instagram-Späher Fehler: {type(e).__name__} {str(e)[:300]}",
            )
        except Exception:
            pass
        sys.exit(1)

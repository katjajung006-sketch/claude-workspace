#!/usr/bin/env python3
# Rendert EIN Teach+Freebie-Karussell (/karussell-einstieg) direkt zu fertigen 1080x1350-PNGs.
# Wiederverwendet das freigegebene Design-System aus ../karussell/build.py (NICHT neu designen).
# Zahl-Logik: nur die Teach-Punkte tragen die große Zahl (1–N).
# Problem-, Erkenntnis- und Freebie-Brücke-Slide bekommen statt Zahl einen kleinen Kicker.
# Einfacher Weg: PNG zum direkten Posten — kein PDF, kein Cloudflare, kein Canva.

import os
import subprocess
import sys

KARU = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "karussell")
sys.path.insert(0, KARU)
from build import HEAD, SCRIPT, HANDLE, PILLAR_YOGA, esc  # exaktes Design-System

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTO = os.path.join(KARU, "katja.jpg")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

KICKER_CSS = (".content-slide .kicker{font-family:'DM Sans',sans-serif;font-weight:500;"
              "font-size:24px;letter-spacing:.24em;text-transform:uppercase;"
              "color:var(--clay);margin-bottom:28px;}\n")
HEAD_K = HEAD.replace("</style>", KICKER_CSS + "</style>")

CAR = {
    "slug": "yoga-nicht-beweglich-einstieg",
    "eyebrow": PILLAR_YOGA,
    "cover": {
        "hook": "Du musst nicht beweglich sein, um mit Yoga anzufangen.",
        "sub": "Du musst dich nur nicht länger übergehen wollen.",
    },
    # kind="label": Kicker statt Zahl · kind="step": große Zahl (durchnummeriert 1..4)
    "content": [
        {"kind": "label", "kicker": "Kennst du das", "text": "Die meisten Yoga-Videos zeigen Frauen, die sich mühelos verbiegen. Du schaust zu und denkst: Nicht mein Körper. Nicht meine Zeit. Und klickst weg."},
        {"kind": "step", "text": "Beweglichkeit ist kein Eintrittspreis. Yoga beginnt nicht im Körper, der schon alles kann — sondern in dem, der wieder spüren darf."},
        {"kind": "step", "text": "Du musst keine Haltung perfekt halten. Du darfst dich hinsetzen, atmen und merken: Ich bin noch da."},
        {"kind": "step", "text": "Die Übungen, die wirklich etwas verändern, sehen nach fast nichts aus. Beine an die Wand. Hand auf den Bauch. Langsam ausatmen."},
        {"kind": "step", "text": "Und es muss nicht lang sein. 3 Minuten reichen, damit dein Körper kurz aus dem Funktionieren aussteigt."},
        {"kind": "label", "kicker": "Neu gedacht", "text": "Vielleicht ist Yoga für dich nicht der Weg, beweglicher zu werden. Vielleicht ist es der Weg, dich im eigenen Alltag wieder zu bemerken."},
        {"kind": "label", "kicker": "Dein erster Schritt", "text": "Der erste Schritt ist kleiner, als du denkst: einmal ehrlich spüren, wie es dir geht. Genau dafür gibt's den Funktionsmodus-Check — 7 Zeichen + deine erste 3-Minuten-Rückkehr."},
    ],
    "close": {
        "relief": "Du musst nicht mehr leisten, um zurückzufinden. Du darfst einfach anfangen, wieder hinzuspüren.",
        "cta": "Kommentiere ANKOMMEN — ich schicke dir den Funktionsmodus-Check, deinen ersten Schritt zurück zu dir.",
    },
}


def build_html(c, photo_uri):
    n = 1
    out = [HEAD_K]
    out.append(f'''<section class="slide cover active" data-slide="{n}">
<img class="photo" src="{photo_uri}" alt="">
<div class="scrim"></div>
<div class="bottom">
<h1>{esc(c["cover"]["hook"])}</h1>
<div class="sub">{esc(c["cover"]["sub"])}</div>
</div></section>''')
    step_no = 0
    for item in c["content"]:
        n += 1
        if item["kind"] == "step":
            step_no += 1
            inner = f'<div class="num">{step_no}</div>\n<div class="body"><p>{esc(item["text"])}</p></div>'
        else:
            inner = f'<div class="body"><div class="kicker">{esc(item["kicker"])}</div><p>{esc(item["text"])}</p></div>'
        out.append(f'''<section class="slide content-slide" data-slide="{n}">
{inner}
<div class="footer">{HANDLE}</div>
</section>''')
    n += 1
    out.append(f'''<section class="slide close" data-slide="{n}">
<img class="photo" src="{photo_uri}" alt="">
<div class="scrim"></div>
<div class="bottom">
<div class="relief">{esc(c["close"]["relief"])}</div>
<div class="cta">{esc(c["close"]["cta"])}</div>
</div></section>''')
    out.append(SCRIPT)
    return "\n".join(out), n


def main():
    photo_uri = "file://" + PHOTO
    folder = os.path.join(HERE, CAR["slug"])
    os.makedirs(folder, exist_ok=True)
    html_str, total = build_html(CAR, photo_uri)
    html_path = os.path.join(folder, "index.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_str)
    for s in range(1, total + 1):
        out_png = os.path.join(folder, f"slide{s:02d}.png")
        url = f"file://{html_path}?slide={s}"
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", "--window-size=1080,1350",
            "--virtual-time-budget=5000", f"--screenshot={out_png}", url,
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"{CAR['slug']}: {total} Slides -> {folder}")


if __name__ == "__main__":
    main()

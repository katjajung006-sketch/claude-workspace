#!/usr/bin/env python3
# Rendert EIN Tutorial-Karussell (/karussell-uebung) direkt zu fertigen 1080x1350-PNGs.
# Wiederverwendet das freigegebene Design-System aus ../karussell/build.py (NICHT neu designen).
# Unterschied zum Wochen-Format: nur die echten SCHRITTE tragen eine große Zahl (1–4).
# Einordnung + Zusammenfassung bekommen statt Zahl einen kleinen, ruhigen Kicker.
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

# Kicker im Brand-Stil (DM Sans, Versalien, Clay) — wird nur dem HEAD hinzugefügt, Rest bleibt identisch.
KICKER_CSS = (".content-slide .kicker{font-family:'DM Sans',sans-serif;font-weight:500;"
              "font-size:24px;letter-spacing:.24em;text-transform:uppercase;"
              "color:var(--clay);margin-bottom:28px;}\n")
HEAD_K = HEAD.replace("</style>", KICKER_CSS + "</style>")

CAR = {
    "slug": "abend-koerper-muede-kopf-laeuft",
    "eyebrow": PILLAR_YOGA,
    "cover": {
        "hook": "3 Minuten für den Abend, an dem dein Körper müde ist – dein Kopf aber weiterläuft.",
        "sub": "Keine Übung zum Können. Nur ein Signal an deinen Körper: Der Tag ist vorbei.",
    },
    # kind="label": Kicker statt Zahl · kind="step": große Zahl (durchnummeriert 1..4)
    "content": [
        {"kind": "label", "kicker": "Warum", "text": "Dein Körper hat den ganzen Tag gehalten. Er braucht jetzt keine neue Aufgabe. Er braucht ein Zeichen: Der Tag ist vorbei."},
        {"kind": "step", "text": "Setz dich auf die Bettkante oder aufs Sofa. Beide Füße auf den Boden. Nicht schön. Nur fest."},
        {"kind": "step", "text": "Zieh die Schultern einmal hoch zu den Ohren – und lass sie fallen. Spür, wie viel du heute getragen hast."},
        {"kind": "step", "text": "Neige den Kopf langsam zur Seite. Kein Ziehen. Nur das Gewicht deines Kopfes. Dann langsam zur anderen Seite."},
        {"kind": "step", "text": "Atme dreimal länger aus als ein. Als würdest du mit jedem Ausatmen den Tag hinter dir lassen."},
        {"kind": "label", "kicker": "Kurz gefasst", "text": "Hinsetzen. Schultern fallen lassen. Kopf zur Seite. Länger ausatmen. So sagst du deinem Körper: Der Tag ist vorbei."},
    ],
    "close": {
        "relief": "Du musst den Tag nicht zu Ende bringen, um anzukommen. Du darfst einfach aufhören zu tragen.",
        "cta": "Speicher dir das – für den Abend, an dem du müde bist, aber trotzdem weitermachst.",
    },
}


def build_html(c, photo_uri):
    n = 1
    out = [HEAD_K]
    out.append(f'''<section class="slide cover active" data-slide="{n}">
<img class="photo" src="{photo_uri}" alt="">
<div class="scrim"></div>
<div class="bottom">
<div class="eyebrow">{esc(c["eyebrow"])}</div>
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

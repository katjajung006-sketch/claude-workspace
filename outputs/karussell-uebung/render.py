#!/usr/bin/env python3
# Rendert EIN Tutorial-Karussell (/karussell-uebung) direkt zu fertigen 1080x1350-PNGs.
# Wiederverwendet das freigegebene Design-System aus ../karussell/build.py (NICHT neu designen).
# Einfacher Weg: PNG zum direkten Posten — kein PDF, kein Cloudflare, kein Canva.

import os
import subprocess
import sys

KARU = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "karussell")
sys.path.insert(0, KARU)
from build import build_html, PILLAR_YOGA  # exaktes Design-System wiederverwenden

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTO = os.path.join(KARU, "katja.jpg")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CAR = {
    "slug": "abend-koerper-muede-kopf-laeuft",
    "eyebrow": PILLAR_YOGA,
    "cover": {
        "hook": "3 Minuten für den Abend, an dem dein Körper müde ist – dein Kopf aber weiterläuft.",
        "sub": "Keine Übung zum Können. Nur ein Signal an deinen Körper: Der Tag ist vorbei.",
    },
    "content": [
        "Dein Körper hat den ganzen Tag gehalten. Er braucht jetzt keine neue Aufgabe. Er braucht ein Zeichen: Der Tag ist vorbei.",
        "Setz dich auf die Bettkante oder aufs Sofa. Beide Füße auf den Boden. Nicht schön. Nur fest.",
        "Zieh die Schultern einmal hoch zu den Ohren – und lass sie fallen. Spür, wie viel du heute getragen hast.",
        "Neige den Kopf langsam zur Seite. Kein Ziehen. Nur das Gewicht deines Kopfes. Dann langsam zur anderen Seite.",
        "Atme dreimal länger aus als ein. Als würdest du mit jedem Ausatmen den Tag hinter dir lassen.",
        "Hinsetzen. Schultern fallen lassen. Kopf zur Seite. Länger ausatmen. So sagst du deinem Körper: Der Tag ist vorbei.",
    ],
    "close": {
        "relief": "Du musst den Tag nicht zu Ende bringen, um anzukommen. Du darfst einfach aufhören zu tragen.",
        "cta": "Speicher dir das – für den Abend, an dem du müde bist, aber trotzdem weitermachst.",
    },
}


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

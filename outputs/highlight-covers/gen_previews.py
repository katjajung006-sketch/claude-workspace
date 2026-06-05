#!/usr/bin/env python3
# Rendert 3 Vorschau-Richtungen für Katjas Instagram Story-Highlight-Cover.
# Zeigt die 7 Cover als KREISE (so wie sie in der Highlight-Leiste erscheinen).
# HTML/CSS -> headless Chrome Screenshot. Brandfarben + Libre Baskerville / DM Sans.

import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Brandfarben
CREME = "#F4EFE7"
SAND = "#D8C7B2"
TON = "#9A7461"
ESPRESSO = "#3A2D28"
SALBEI = "#A8AEA0"
TERRA = "#B66F55"

# Die 7 Highlights (Reihenfolge wie in Notion)
# name = Caption unter dem Cover (IG-Label, nicht Teil des Covers)
# word = Ein-Wort-Variante (Richtung A / C)
HIGHLIGHTS = [
    {"name": "Starte hier",     "word": "hier",    "icon": "sunrise"},
    {"name": "Über mich",       "word": "ich",     "icon": "person"},
    {"name": "Funktionsmodus",  "word": "modus",   "icon": "loop"},
    {"name": "Yoga 40+",        "word": "yoga",    "icon": "seated"},
    {"name": "3-Minuten-Yoga",  "word": "3 min",   "icon": "clock"},
    {"name": "Wahre Sätze",     "word": "sätze",   "icon": "quote"},
    {"name": "Angebot",         "word": "leben",   "icon": "leaf"},
]

# Schlanke Strich-Icons (stroke = Tonbraun), 100x100 viewBox, runde Enden.
def icon_svg(key, color=TON, sw=4.2):
    base = f'stroke="{color}" stroke-width="{sw}" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    icons = {
        # Sonnenaufgang — Anfang, Morgen
        "sunrise": f'''<svg viewBox="0 0 100 100" width="46%" >
            <g {base}>
              <line x1="18" y1="66" x2="82" y2="66"/>
              <path d="M30 66 a20 20 0 0 1 40 0"/>
              <line x1="50" y1="30" x2="50" y2="22"/>
              <line x1="29" y1="39" x2="24" y2="34"/>
              <line x1="71" y1="39" x2="76" y2="34"/>
            </g></svg>''',
        # Person — Über mich
        "person": f'''<svg viewBox="0 0 100 100" width="40%">
            <g {base}>
              <circle cx="50" cy="38" r="13"/>
              <path d="M27 74 a23 20 0 0 1 46 0"/>
            </g></svg>''',
        # Endlos-Schleife — Funktionieren ohne Aufhören
        "loop": f'''<svg viewBox="0 0 100 100" width="46%">
            <g {base}>
              <path d="M28 38 a26 22 0 1 1 -2 24"/>
              <polyline points="20,30 28,38 36,30"/>
            </g></svg>''',
        # Sitzende Figur — Yoga
        "seated": f'''<svg viewBox="0 0 100 100" width="48%">
            <g {base}>
              <circle cx="50" cy="30" r="9"/>
              <path d="M50 44 L36 70 L64 70 Z"/>
              <line x1="30" y1="70" x2="70" y2="70"/>
            </g></svg>''',
        # Uhr — 3 Minuten
        "clock": f'''<svg viewBox="0 0 100 100" width="46%">
            <g {base}>
              <circle cx="50" cy="52" r="26"/>
              <line x1="50" y1="52" x2="50" y2="36"/>
              <line x1="50" y1="52" x2="62" y2="58"/>
            </g></svg>''',
        # Anführungszeichen — Wahre Sätze
        "quote": f'''<svg viewBox="0 0 100 100" width="46%">
            <g {base}>
              <path d="M34 40 q-10 6 -10 20 h12 v-12 h-10"/>
              <path d="M64 40 q-10 6 -10 20 h12 v-12 h-10"/>
            </g></svg>''',
        # Blatt/Zweig — Angebot (Rückkehr, Wachstum)
        "leaf": f'''<svg viewBox="0 0 100 100" width="44%">
            <g {base}>
              <path d="M50 74 C30 60 30 34 50 26 C70 34 70 60 50 74 Z"/>
              <line x1="50" y1="40" x2="50" y2="74"/>
            </g></svg>''',
    }
    return icons.get(key, "")


def circle_cover(direction, h):
    """Gibt das innere HTML eines Cover-Kreises für eine Richtung zurück."""
    if direction == "A":
        # Ein Wort, Sandbeige, Espresso-Serif
        return f'<div class="circle" style="background:{SAND}">' \
               f'<span class="word">{h["word"]}</span></div>'
    if direction == "B":
        # Nur Strich-Icon, Cremeweiß
        return f'<div class="circle" style="background:{CREME}">' \
               f'{icon_svg(h["icon"])}</div>'
    if direction == "C":
        # Icon + Wort, Sandbeige
        return f'<div class="circle col" style="background:{SAND}">' \
               f'{icon_svg(h["icon"], color=ESPRESSO, sw=4.0)}' \
               f'<span class="word small">{h["word"]}</span></div>'
    return ""


TITLES = {
    "A": "Richtung A · Ein Wort — ruhig, warm, sofort lesbar",
    "B": "Richtung B · Strichsymbol — wortlos, designstark, eine stille Reihe",
    "C": "Richtung C · Symbol + Wort — Symbol fürs Auge, Wort für die Klarheit",
}


def build_page(direction):
    items = ""
    for h in HIGHLIGHTS:
        items += f'''<div class="item">
            <div class="ring">{circle_cover(direction, h)}</div>
            <div class="label">{h["name"]}</div>
        </div>'''
    return f'''<!doctype html><html><head><meta charset="utf-8">
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=DM+Sans:wght@400;500&display=swap');
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      body {{ width:2520px; height:620px; background:#e9e6e1;
              font-family:'DM Sans',sans-serif; padding:46px 60px; }}
      .title {{ font-family:'Libre Baskerville',serif; color:{ESPRESSO};
                font-size:34px; margin-bottom:38px; letter-spacing:.2px; }}
      .row {{ display:flex; gap:44px; justify-content:flex-start; }}
      .item {{ display:flex; flex-direction:column; align-items:center; width:300px; }}
      .ring {{ width:300px; height:300px; border-radius:50%;
               padding:7px; background:#cdbfae;
               display:flex; align-items:center; justify-content:center; }}
      .circle {{ width:100%; height:100%; border-radius:50%;
                 display:flex; align-items:center; justify-content:center;
                 overflow:hidden; }}
      .circle.col {{ flex-direction:column; gap:10px; }}
      .word {{ font-family:'Libre Baskerville',serif; color:{ESPRESSO};
               font-size:62px; line-height:1; }}
      .word.small {{ font-size:40px; }}
      .label {{ font-family:'DM Sans',sans-serif; color:#7a7066;
                font-size:24px; margin-top:20px; }}
    </style></head>
    <body>
      <div class="title">{TITLES[direction]}</div>
      <div class="row">{items}</div>
    </body></html>'''


def render(direction):
    html_path = os.path.join(HERE, f"_preview_{direction}.html")
    png_path = os.path.join(HERE, f"vorschau-{direction}.png")
    with open(html_path, "w") as f:
        f.write(build_page(direction))
    url = "file://" + html_path
    subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=1", "--window-size=2520,620",
        "--default-background-color=00000000",
        "--virtual-time-budget=6000", f"--screenshot={png_path}", url,
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("ok:", png_path)


if __name__ == "__main__":
    for d in ("A", "B", "C"):
        render(d)

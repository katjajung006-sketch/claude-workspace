#!/usr/bin/env python3
# Finale Instagram Story-Highlight-Cover für Katja.
# Richtung: B (nur Strichsymbol, kein Wort) auf Sandbeige-Hintergrund (von C).
# Espresso-Symbole auf #D8C7B2. Vollbild 1080x1920, Symbol mittig im Kreis-Safe-Zone.
# Output: einzelne PNGs (für IG-Upload) + ein 7-seitiges PDF (editierbar in Canva).

import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "final")
os.makedirs(OUT, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

SAND = "#D8C7B2"      # Hintergrund (Hauptfarbe)
ESPRESSO = "#3A2D28"  # Symbolfarbe

HIGHLIGHTS = [
    {"slug": "01-starte-hier",    "name": "Starte hier",    "icon": "sunrise"},
    {"slug": "02-ueber-mich",     "name": "Über mich",      "icon": "person"},
    {"slug": "03-funktionsmodus", "name": "Funktionsmodus", "icon": "loop"},
    {"slug": "04-yoga-40plus",    "name": "Yoga 40+",       "icon": "seated"},
    {"slug": "05-3-minuten-yoga", "name": "3-Minuten-Yoga", "icon": "clock"},
    {"slug": "06-wahre-saetze",   "name": "Wahre Sätze",    "icon": "quote"},
    {"slug": "07-angebot",        "name": "Angebot",        "icon": "leaf"},
]

SW = 4.6  # Strichstärke in viewBox-Einheiten (0..100)

def icon_svg(key, size_pct=34):
    base = (f'stroke="{ESPRESSO}" stroke-width="{SW}" fill="none" '
            f'stroke-linecap="round" stroke-linejoin="round"')
    paths = {
        "sunrise": '''
              <line x1="18" y1="66" x2="82" y2="66"/>
              <path d="M30 66 a20 20 0 0 1 40 0"/>
              <line x1="50" y1="30" x2="50" y2="22"/>
              <line x1="29" y1="39" x2="24" y2="34"/>
              <line x1="71" y1="39" x2="76" y2="34"/>''',
        "person": '''
              <circle cx="50" cy="38" r="13"/>
              <path d="M27 74 a23 20 0 0 1 46 0"/>''',
        "loop": '''
              <path d="M28 38 a26 22 0 1 1 -2 24"/>
              <polyline points="20,30 28,38 36,30"/>''',
        "seated": '''
              <circle cx="50" cy="30" r="9"/>
              <path d="M50 44 L36 70 L64 70 Z"/>
              <line x1="30" y1="70" x2="70" y2="70"/>''',
        "clock": '''
              <circle cx="50" cy="52" r="26"/>
              <line x1="50" y1="52" x2="50" y2="36"/>
              <line x1="50" y1="52" x2="62" y2="58"/>''',
        "leaf": '''
              <path d="M50 76 C28 60 28 32 50 24 C72 32 72 60 50 76 Z"/>
              <line x1="50" y1="40" x2="50" y2="76"/>''',
    }
    g = f'<g {base}>{paths[key]}</g>'
    return f'<svg viewBox="0 0 100 100" style="width:{size_pct}vw">{g}</svg>'


# Google Fonts für das typografische Anführungszeichen (Wahre Sätze)
FONT_IMPORT = ("@import url('https://fonts.googleapis.com/css2?"
               "family=Libre+Baskerville:wght@700&display=swap');")


def content_html(h):
    # Wahre Sätze = großes Serif-Anführungszeichen statt Strich-Icon
    if h["icon"] == "quote":
        return '<div class="quote">“</div>'
    return icon_svg(h["icon"])


def cover_div(h):
    return (f'<section class="cover">{content_html(h)}</section>')


# ---- Einzelne PNGs ----
def png_html(h):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
      {FONT_IMPORT}
      *{{margin:0;padding:0;box-sizing:border-box}}
      html,body{{width:1080px;height:1920px}}
      .cover{{width:1080px;height:1920px;background:{SAND};
              display:flex;align-items:center;justify-content:center;
              -webkit-print-color-adjust:exact;print-color-adjust:exact}}
      svg{{display:block}}
      .quote{{font-family:'Libre Baskerville',serif;color:{ESPRESSO};
              font-size:560px;line-height:1;height:340px;
              display:flex;align-items:center;justify-content:center}}
    </style></head><body>{cover_div(h)}</body></html>'''


def render_pngs():
    for h in HIGHLIGHTS:
        hp = os.path.join(HERE, f"_f_{h['slug']}.html")
        with open(hp, "w") as f:
            f.write(png_html(h))
        out = os.path.join(OUT, f"{h['slug']}.png")
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", "--window-size=1080,1920",
            "--virtual-time-budget=4000", f"--screenshot={out}", "file://" + hp,
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("png:", out)


# ---- Ein PDF, 7 Seiten (editierbar in Canva) ----
def render_pdf():
    sections = "".join(cover_div(h) for h in HIGHLIGHTS)
    html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
      {FONT_IMPORT}
      @page{{size:1080px 1920px;margin:0}}
      *{{margin:0;padding:0;box-sizing:border-box}}
      .cover{{width:1080px;height:1920px;background:{SAND};
              display:flex;align-items:center;justify-content:center;
              page-break-after:always;
              -webkit-print-color-adjust:exact;print-color-adjust:exact}}
      svg{{display:block}}
      .quote{{font-family:'Libre Baskerville',serif;color:{ESPRESSO};
              font-size:560px;line-height:1;height:340px;
              display:flex;align-items:center;justify-content:center}}
    </style></head><body>{sections}</body></html>'''
    hp = os.path.join(HERE, "_f_all.html")
    with open(hp, "w") as f:
        f.write(html)
    out = os.path.join(OUT, "highlight-cover.pdf")
    subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        "--virtual-time-budget=4000", f"--print-to-pdf={out}", "file://" + hp,
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("pdf:", out)


if __name__ == "__main__":
    render_pngs()
    render_pdf()

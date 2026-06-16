#!/usr/bin/env python3
# Reelcover-Vorlage (neu, 2026-06-16) fuer die Yoga-Serie /reel-yoga + /reel-yoga-wirkung.
# Idee 1: grosser Neugier-Satz als Blickfang, "3 MIN" nur als kleines, frei verschiebbares Eck-Badge.
# Zwei Varianten: (1) Foto + dunkler Verlauf unten  (2) schlicht einfarbig Sandbeige.
# Look = Marken-Welt: Libre Baskerville (Hook) + DM Sans (Badge/Handle), Sandbeige/Espresso/Cream.
# 1080x1920. Output: Preview-PNGs + 2-seitiges PDF (editierbar in Canva, wie Highlight-Cover/Story-Vorlagen).

import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "final")
os.makedirs(OUT, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

SAND = "#D8C7B2"; CREAM = "#F4EFE7"; CLAY = "#9A7461"; ESPRESSO = "#3A2D28"; TAUPE = "#C7B49E"

FONT = ("@import url('https://fonts.googleapis.com/css2?"
        "family=Libre+Baskerville:ital,wght@0,400;0,700;1,400"
        "&family=DM+Sans:wght@400;500;600&display=swap');")

CLOCK = ('<svg class="clock" width="44" height="44" viewBox="0 0 24 24" fill="none" '
         'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
         '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path></svg>')

# Jede Variante: bg-Klasse, Hook-Beispieltext (Platzhalter — in Canva ersetzen), Badge-Stil.
VARIANTS = [
    {
        "slug": "01-foto-verlauf", "cls": "foto",
        "hook": "Wenn dein Kopf<br>nicht aufhört",
    },
    {
        "slug": "02-einfarbig", "cls": "solid",
        "hook": "Wenn du nur<br>noch funktionierst",
    },
]

CSS = f'''
  {FONT}
  *{{margin:0;padding:0;box-sizing:border-box}}
  .cover{{width:1080px;height:1920px;position:relative;overflow:hidden;
          page-break-after:always;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
  .cover.foto{{background:{TAUPE}}}
  .cover.solid{{background:{SAND}}}
  .scrim{{position:absolute;left:0;right:0;bottom:0;height:62%;
          background:linear-gradient(to bottom, rgba(58,45,40,0) 0%, rgba(58,45,40,.30) 42%, rgba(58,45,40,.86) 100%)}}
  .badge{{position:absolute;top:96px;left:90px;display:inline-flex;align-items:center;gap:14px;
          padding:20px 36px 20px 30px;border-radius:999px;
          font-family:'DM Sans',sans-serif;font-weight:600;font-size:40px;letter-spacing:.10em}}
  .badge .clock{{width:42px;height:42px}}
  .cover.foto .badge{{background:{CREAM};color:{ESPRESSO}}}
  .cover.solid .badge{{background:{ESPRESSO};color:{CREAM}}}
  .hook{{position:absolute;left:92px;right:120px;bottom:168px;
         font-family:'Libre Baskerville',serif;font-weight:400;font-size:104px;line-height:1.2}}
  .cover.foto .hook{{color:{CREAM}}}
  .cover.solid .hook{{color:{ESPRESSO}}}
  .handle{{position:absolute;left:94px;bottom:74px;
           font-family:'DM Sans',sans-serif;font-weight:500;font-size:34px;letter-spacing:.04em}}
  .cover.foto .handle{{color:rgba(244,239,231,.92)}}
  .cover.solid .handle{{color:{CLAY}}}
'''


def cover_div(v):
    scrim = '<div class="scrim"></div>' if v["cls"] == "foto" else ""
    return (f'<section class="cover {v["cls"]}">{scrim}'
            f'<div class="badge">{CLOCK}<span>3 MIN</span></div>'
            f'<div class="hook">{v["hook"]}</div>'
            f'<div class="handle">@yoga.statt.funktionieren</div></section>')


def render_pngs():
    for v in VARIANTS:
        hp = os.path.join(HERE, f"_c_{v['slug']}.html")
        html = (f'<!doctype html><html><head><meta charset="utf-8">'
                f'<style>{CSS}</style></head><body>{cover_div(v)}</body></html>')
        with open(hp, "w") as f:
            f.write(html)
        out = os.path.join(OUT, f"{v['slug']}.png")
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", "--window-size=1080,1920",
            "--virtual-time-budget=4000", f"--screenshot={out}", "file://" + hp,
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove(hp)
        print("png:", out)


def render_pdf():
    sections = "".join(cover_div(v) for v in VARIANTS)
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>'
            f'@page{{size:1080px 1920px;margin:0}}{CSS}</style></head>'
            f'<body>{sections}</body></html>')
    hp = os.path.join(HERE, "_c_all.html")
    with open(hp, "w") as f:
        f.write(html)
    out = os.path.join(OUT, "reelcover-vorlagen.pdf")
    subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        "--virtual-time-budget=4000", f"--print-to-pdf={out}", "file://" + hp,
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(hp)
    print("pdf:", out)


if __name__ == "__main__":
    render_pngs()
    render_pdf()

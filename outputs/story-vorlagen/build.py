#!/usr/bin/env python3
# Instagram-Story-Vorlagen für @yoga.statt.funktionieren — eine Vorlage je Story-Typ.
# Look = Marken-Welt: Sandbeige/Creme, Libre Baskerville + DM Sans, Espresso-Text.
# 1080x1920. Output: einzelne Preview-PNGs + ein mehrseitiges PDF (editierbar in Canva).
# Pipeline wie Highlight-Cover/Karussell: HTML/CSS -> headless Chrome.

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

# Jede Vorlage = ein Story-Typ aus den Bausteinen A–H. Platzhaltertexte zeigen Stimme + Stil.
FRAMES = [
    {
        "slug": "01-wahrer-satz", "bg": "bg-sand", "eyebrow": "WAHRER SATZ",
        "body": '<p class="satz">Vielleicht bist du nicht zu müde.<br>Vielleicht hast du nur zu lange über dich hinweggesehen.</p>',
    },
    {
        "slug": "02-spuer-check", "bg": "bg-cream", "eyebrow": "SPÜR-CHECK",
        "body": ('<p class="frage">Wie war dein Tag — ganz ehrlich?</p>'
                 '<div class="optbox">nur funktioniert</div>'
                 '<div class="optbox">kurz bei mir gewesen</div>'),
    },
    {
        "slug": "03-mini-impuls", "bg": "bg-sand", "eyebrow": "MINI-IMPULS",
        "body": ('<p class="satz">Dein Nacken ist fest und dein Kopf voll.</p>'
                 '<div class="rule"></div>'
                 '<p class="step">Atme einmal langsam aus — und lass die Schultern dabei sinken.</p>'),
    },
    {
        "slug": "04-leiser-take", "bg": "bg-cream", "eyebrow": "LEISER TAKE", "align": "left",
        "body": ('<div class="accent"></div>'
                 '<p class="take">Mehr Druck war noch nie die Antwort.<br>Manchmal ist es Aufhören.</p>'),
    },
    {
        "slug": "05-frage-box", "bg": "bg-cream", "eyebrow": "FRAGE",
        "body": ('<p class="frage">Was übergehst du gerade an dir?</p>'
                 '<div class="fragebox">deine Antwort …</div>'),
    },
    {
        "slug": "06-einladung", "bg": "bg-sand", "eyebrow": "EINLADUNG",
        "body": ('<p class="satz">Drei Minuten, in denen du nichts musst.</p>'
                 '<div class="cta-pill">Funktionsmodus-Check holen</div>'
                 '<p class="link">check.katjajung.com</p>'),
    },
    {
        "slug": "07-behind-the-scenes", "bg": "bg-taupe", "eyebrow": "BEHIND THE SCENES",
        "align": "bts",
        "body": ('<div class="bts-card">Hier entsteht gerade, woran ich glaube — leise, neben allem anderen.</div>'),
    },
]

CSS = f'''
  {FONT}
  *{{margin:0;padding:0;box-sizing:border-box}}
  .frame{{width:1080px;height:1920px;position:relative;overflow:hidden;
          display:flex;flex-direction:column;align-items:center;justify-content:center;
          text-align:center;padding:0 120px;page-break-after:always;
          -webkit-print-color-adjust:exact;print-color-adjust:exact}}
  .bg-sand{{background:{SAND}}} .bg-cream{{background:{CREAM}}} .bg-taupe{{background:{TAUPE}}}
  .eyebrow{{position:absolute;top:172px;left:0;right:0;text-align:center;
            font-family:'DM Sans',sans-serif;font-weight:500;font-size:28px;
            letter-spacing:.28em;text-transform:uppercase;color:{CLAY}}}
  .satz{{font-family:'Libre Baskerville',serif;font-weight:400;font-size:56px;
         line-height:1.5;color:{ESPRESSO};max-width:920px}}
  .frage{{font-family:'Libre Baskerville',serif;font-weight:400;font-size:56px;
          line-height:1.42;color:{ESPRESSO};max-width:820px}}
  .step{{font-family:'DM Sans',sans-serif;font-weight:400;font-size:40px;
         line-height:1.5;color:{ESPRESSO};max-width:760px}}
  .rule{{width:120px;height:2px;background:{ESPRESSO};opacity:.38;margin:54px 0}}
  .optbox{{border:2.5px solid {ESPRESSO};border-radius:64px;width:640px;padding:36px 0;
           margin-top:40px;font-family:'DM Sans',sans-serif;font-weight:500;
           font-size:40px;color:{ESPRESSO}}}
  /* Leiser Take: linksbündig, Akzent-Balken */
  .frame.left{{align-items:flex-start;text-align:left;padding:0 130px}}
  .accent{{width:96px;height:6px;background:{ESPRESSO};margin-bottom:46px}}
  .take{{font-family:'Libre Baskerville',serif;font-weight:700;font-size:62px;
         line-height:1.36;color:{ESPRESSO};max-width:860px;text-align:left}}
  /* Frage-Box-Platzhalter */
  .fragebox{{border:2.5px solid {ESPRESSO};border-radius:28px;width:760px;padding:56px 40px;
             margin-top:50px;font-family:'DM Sans',sans-serif;font-weight:400;
             font-size:36px;color:rgba(58,45,40,.45)}}
  /* Einladung-CTA */
  .cta-pill{{background:{ESPRESSO};color:{CREAM};border-radius:64px;padding:36px 70px;
             margin-top:56px;font-family:'DM Sans',sans-serif;font-weight:600;font-size:40px}}
  .link{{font-family:'DM Sans',sans-serif;font-weight:500;font-size:32px;color:{CLAY};
         margin-top:30px;letter-spacing:.04em}}
  /* BTS: Foto-/B-Roll-Fläche, Caption-Karte unten */
  .frame.bts{{justify-content:flex-end;padding:0 120px 230px}}
  .frame.bts .eyebrow{{color:#5A4A40}}
  .bts-card{{background:{CREAM};border-radius:28px;padding:56px 58px;max-width:840px;
             font-family:'DM Sans',sans-serif;font-weight:400;font-size:40px;
             line-height:1.5;color:{ESPRESSO}}}
'''


def frame_div(fr):
    align = fr.get("align", "")
    cls = "frame " + fr["bg"]
    if align == "left":
        cls += " left"
    elif align == "bts":
        cls += " bts"
    return (f'<section class="{cls}">'
            f'<div class="eyebrow">{fr["eyebrow"]}</div>{fr["body"]}</section>')


def render_pngs():
    for fr in FRAMES:
        hp = os.path.join(HERE, f"_f_{fr['slug']}.html")
        html = (f'<!doctype html><html><head><meta charset="utf-8">'
                f'<style>{CSS}</style></head><body>{frame_div(fr)}</body></html>')
        with open(hp, "w") as f:
            f.write(html)
        out = os.path.join(OUT, f"{fr['slug']}.png")
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", "--window-size=1080,1920",
            "--virtual-time-budget=4000", f"--screenshot={out}", "file://" + hp,
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove(hp)
        print("png:", out)


def render_pdf():
    sections = "".join(frame_div(fr) for fr in FRAMES)
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>'
            f'@page{{size:1080px 1920px;margin:0}}{CSS}</style></head>'
            f'<body>{sections}</body></html>')
    hp = os.path.join(HERE, "_f_all.html")
    with open(hp, "w") as f:
        f.write(html)
    out = os.path.join(OUT, "story-vorlagen.pdf")
    subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        "--virtual-time-budget=4000", f"--print-to-pdf={out}", "file://" + hp,
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(hp)
    print("pdf:", out)


if __name__ == "__main__":
    render_pngs()
    render_pdf()

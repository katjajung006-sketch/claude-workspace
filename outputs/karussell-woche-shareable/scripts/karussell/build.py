#!/usr/bin/env python3
# Rendert Instagram-Karussells aus HTML/CSS zu 1080x1350-PNGs (Vorschau).
# Design-System: Foto-Cover -> farbige Inhalts-Slides (grosse ruhige Zahl) -> Foto-Schluss.
# Fuer den editierbaren Canva-Import wird stattdessen build_pdf.py genutzt (echter Text).
#
# ====================== ANPASSEN ======================
# 1) HANDLE unten auf deinen Instagram-Namen setzen.
# 2) Dein Foto als photo.jpg in diesen Ordner legen.
# 3) CAROUSELS mit deinen 7 Karussells fuellen (Demo-Eintraege unten ersetzen).
# 4) Optional: Farben/Schriften im HEAD-Block (--sand, --cream, Google Fonts).
# 5) CHROME-Pfad falls noetig (Windows/Linux) anpassen.
# ======================================================

import html
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTO = os.path.join(HERE, "photo.jpg")

# Pfad zu Google Chrome (Headless-Rendering).
# macOS:   /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
# Linux:   google-chrome  (oder /usr/bin/google-chrome)
# Windows: C:/Program Files/Google/Chrome/Application/chrome.exe
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Inhaltssäulen -> Eyebrow-Text (deine Content-Säulen eintragen)
PILLAR_A = "SÄULE A"
PILLAR_B = "SÄULE B"

HANDLE = "[@DEINHANDLE]"

# ---------------------------------------------------------------------------
# DEMO-INHALT — durch deine 7 echten Karussells ersetzen.
# Struktur pro Karussell siehe Kommentare. slug = 01..07 + kurzer kebab-case-Name.
# ---------------------------------------------------------------------------
CAROUSELS = [
    {
        "slug": "01-beispiel-thema",
        "eyebrow": PILLAR_A,
        "cover": {
            "hook": "Dein starker erster Satz steht hier.",
            "sub": "Ein ruhiger Zweizeiler, der den Hook trägt.",
        },
        "content": [
            "Slide-Gedanke 1 — ein kurzer, konkreter Satz.",
            "Slide-Gedanke 2 — EIN Gedanke pro Slide, ruhig.",
            "Slide-Gedanke 3 — die grosse Zahl ist Gestaltung, kein Aufzähl-Zwang.",
            "Slide-Gedanke 4 — max. ~2 kurze Sätze.",
            "Slide-Gedanke 5 — der Text trägt, nicht die Zahl.",
        ],
        "close": {
            "relief": "Ein entlastender, wahrer Schlusssatz (kein Motivations-Spruch).",
            "cta": "Speicher dir das — für den Moment, in dem du's brauchst.",
        },
    },
    {
        "slug": "02-zweites-beispiel",
        "eyebrow": PILLAR_B,
        "cover": {
            "hook": "Zweiter Beispiel-Hook für die zweite Content-Säule.",
            "sub": "Kurzer, konkreter Untertitel.",
        },
        "content": [
            "Erster Punkt.",
            "Zweiter Punkt.",
            "Dritter Punkt.",
        ],
        "close": {
            "relief": "Schlusssatz, der entlastet statt zu pushen.",
            "cta": "Wenn dich das trifft: teil es mit jemandem, der es lesen sollte.",
        },
    },
]

HEAD = """<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{--sand:#D8C7B2;--cream:#F4EFE7;--clay:#9A7461;--espresso:#3A2D28;}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{background:#1a1a1a;}
::-webkit-scrollbar{display:none;}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;display:none;font-family:'DM Sans',sans-serif;}
.slide.active{display:block;}
.photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 22%;}
.scrim{position:absolute;inset:0;}
.cover .scrim{background:linear-gradient(to bottom,rgba(58,45,40,.15) 0%,rgba(58,45,40,.35) 48%,rgba(58,45,40,.86) 100%);}
.close .scrim{background:linear-gradient(to bottom,rgba(58,45,40,.30) 0%,rgba(58,45,40,.55) 40%,rgba(58,45,40,.92) 100%);}
.bottom{position:absolute;left:0;right:0;bottom:0;padding:0 96px 110px;}
.eyebrow{font-family:'DM Sans',sans-serif;font-weight:500;font-size:24px;letter-spacing:.24em;text-transform:uppercase;color:var(--sand);margin-bottom:30px;}
.cover h1{font-family:'Libre Baskerville',serif;font-weight:700;font-size:70px;line-height:1.2;color:var(--cream);letter-spacing:-.5px;}
.cover .sub{font-family:'DM Sans',sans-serif;font-weight:400;font-size:30px;line-height:1.45;color:rgba(244,239,231,.82);margin-top:30px;max-width:780px;}
.content-slide{background:var(--sand);}
.content-slide .num{position:absolute;top:84px;right:104px;font-family:'Libre Baskerville',serif;font-weight:700;font-size:290px;line-height:1;color:var(--cream);opacity:.62;letter-spacing:-6px;}
.content-slide .body{position:absolute;left:104px;right:104px;top:50%;transform:translateY(-50%);}
.content-slide .body p{font-family:'Libre Baskerville',serif;font-weight:400;font-size:56px;line-height:1.42;color:var(--espresso);max-width:872px;}
.footer{position:absolute;left:104px;bottom:78px;font-family:'DM Sans',sans-serif;font-weight:500;font-size:23px;letter-spacing:.04em;color:var(--clay);}
.close .relief{font-family:'Libre Baskerville',serif;font-weight:700;font-size:58px;line-height:1.3;color:var(--cream);max-width:872px;}
.close .cta{font-family:'DM Sans',sans-serif;font-weight:500;font-size:30px;line-height:1.45;color:var(--sand);margin-top:34px;}
</style></head><body>
"""

SCRIPT = """
<script>
function show(n){document.querySelectorAll('.slide').forEach(s=>s.classList.remove('active'));
var el=document.querySelector('.slide[data-slide="'+n+'"]');if(el)el.classList.add('active');}
var p=new URLSearchParams(location.search).get('slide');if(p)show(p);
</script></body></html>
"""


def esc(s):
    return html.escape(s, quote=False)


def build_html(c, photo_uri):
    n = 1
    out = [HEAD]
    # cover
    out.append(f'''<section class="slide cover {"active" if n==1 else ""}" data-slide="{n}">
<img class="photo" src="{photo_uri}" alt="">
<div class="scrim"></div>
<div class="bottom">
<h1>{esc(c["cover"]["hook"])}</h1>
<div class="sub">{esc(c["cover"]["sub"])}</div>
</div></section>''')
    # content
    for i, text in enumerate(c["content"], start=1):
        n += 1
        out.append(f'''<section class="slide content-slide" data-slide="{n}">
<div class="num">{i}</div>
<div class="body"><p>{esc(text)}</p></div>
<div class="footer">{HANDLE}</div>
</section>''')
    # close
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
    for c in CAROUSELS:
        folder = os.path.join(HERE, c["slug"])
        os.makedirs(folder, exist_ok=True)
        html_str, total = build_html(c, photo_uri)
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
        print(f"{c['slug']}: {total} Slides")


if __name__ == "__main__":
    main()

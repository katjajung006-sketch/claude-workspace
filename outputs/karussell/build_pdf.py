#!/usr/bin/env python3
# Rendert jedes Karussell als mehrseitiges PDF (echte Textseiten, 1080x1350) via Headless-Chrome.
# Zweck: editierbarer Import nach Canva (import-design-from-url braucht eine oeffentliche Datei).

import html
import os
import subprocess

from build import CAROUSELS, HANDLE

HERE = os.path.dirname(os.path.abspath(__file__))
COVER_BG = os.path.join(HERE, "cover_bg.png")
CLOSE_BG = os.path.join(HERE, "close_bg.png")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTDIR = os.path.join(HERE, "_pdf")


def esc(s):
    return html.escape(s, quote=False)


HEAD = """<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
@page{size:1080px 1350px;margin:0;}
:root{--sand:#D8C7B2;--cream:#F4EFE7;--clay:#9A7461;--espresso:#3A2D28;}
*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
html,body{background:#fff;}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'DM Sans',sans-serif;page-break-after:always;break-after:page;}
.slide:last-child{page-break-after:avoid;break-after:avoid;}
.photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 22%;}
.scrim{position:absolute;inset:0;}
.cover .scrim{background:linear-gradient(to bottom,rgba(58,45,40,.15) 0%,rgba(58,45,40,.35) 48%,rgba(58,45,40,.86) 100%);}
.close .scrim{background:linear-gradient(to bottom,rgba(58,45,40,.30) 0%,rgba(58,45,40,.55) 40%,rgba(58,45,40,.92) 100%);}
.bottom{position:absolute;left:0;right:0;bottom:0;padding:0 96px 110px;}
.eyebrow{font-weight:500;font-size:24px;letter-spacing:.24em;text-transform:uppercase;color:var(--sand);margin-bottom:30px;}
.cover h1{font-family:'Libre Baskerville',serif;font-weight:700;font-size:70px;line-height:1.2;color:var(--cream);letter-spacing:-.5px;}
.cover .sub{font-weight:400;font-size:30px;line-height:1.45;color:rgba(244,239,231,.82);margin-top:30px;max-width:780px;}
.content-slide{background:var(--sand);}
.content-slide .num{position:absolute;top:84px;right:104px;font-family:'Libre Baskerville',serif;font-weight:700;font-size:290px;line-height:1;color:var(--cream);opacity:.62;letter-spacing:-6px;}
.content-slide .body{position:absolute;left:104px;right:104px;top:50%;transform:translateY(-50%);}
.content-slide .body p{font-family:'Libre Baskerville',serif;font-weight:400;font-size:56px;line-height:1.42;color:var(--espresso);max-width:872px;}
.footer{position:absolute;left:104px;bottom:78px;font-weight:500;font-size:23px;letter-spacing:.04em;color:var(--clay);}
.close .relief{font-family:'Libre Baskerville',serif;font-weight:700;font-size:58px;line-height:1.3;color:var(--cream);max-width:872px;}
.close .cta{font-weight:500;font-size:30px;line-height:1.45;color:var(--sand);margin-top:34px;}
</style></head><body>
"""


def slides_html(c, cover_uri, close_uri):
    out = [HEAD]
    out.append(f'''<section class="slide cover">
<img class="photo" src="{cover_uri}" alt="">
<div class="bottom">
<h1>{esc(c["cover"]["hook"])}</h1>
<div class="sub">{esc(c["cover"]["sub"])}</div>
</div></section>''')
    for i, text in enumerate(c["content"], start=1):
        out.append(f'''<section class="slide content-slide">
<div class="num">{i}</div>
<div class="body"><p>{esc(text)}</p></div>
<div class="footer">{HANDLE}</div>
</section>''')
    out.append(f'''<section class="slide close">
<img class="photo" src="{close_uri}" alt="">
<div class="bottom">
<div class="relief">{esc(c["close"]["relief"])}</div>
<div class="cta">{esc(c["close"]["cta"])}</div>
</div></section>''')
    out.append("</body></html>")
    return "\n".join(out)


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    cover_uri = "file://" + COVER_BG
    close_uri = "file://" + CLOSE_BG
    for c in CAROUSELS:
        html_path = os.path.join(OUTDIR, c["slug"] + ".html")
        pdf_path = os.path.join(OUTDIR, c["slug"] + ".pdf")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(slides_html(c, cover_uri, close_uri))
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
            "--virtual-time-budget=6000", f"--print-to-pdf={pdf_path}",
            f"file://{html_path}",
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(c["slug"] + ".pdf")


if __name__ == "__main__":
    main()

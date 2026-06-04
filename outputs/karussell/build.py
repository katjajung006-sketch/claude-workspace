#!/usr/bin/env python3
# Rendert Katjas Instagram-Karussells aus HTML/CSS zu 1080x1350-PNGs.
# Design-System: Foto-Cover -> Sandbeige-Inhalts-Slides (große ruhige Zahl) -> Foto-Schluss.
# Brand-Schriften: Libre Baskerville + DM Sans (Google Fonts). Brand-Sandbeige #D8C7B2.

import html
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTO = os.path.join(HERE, "katja.jpg")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Inhaltssäulen -> Eyebrow-Text
PILLAR_FUNKTION = "DER KÖRPER IM FUNKTIONSMODUS"
PILLAR_YOGA = "YOGA OHNE LEISTUNGSDRUCK"

CAROUSELS = [
    {
        "slug": "01-7-stille-zeichen",
        "eyebrow": PILLAR_FUNKTION,
        "cover": {
            "hook": "7 stille Zeichen, dass du nur noch funktionierst.",
            "sub": "Nicht laut. Nicht dramatisch. Einfach leise da.",
        },
        "content": [
            "Du merkst erst, dass du erschöpft bist, wenn du dich endlich hinsetzt.",
            "Pause machst du erst, wenn alles erledigt ist. Also fast nie.",
            "„Mir geht's gut“ sagst du schneller, als du nachspürst, ob es stimmt.",
            "Dein Atem ist flach, deine Schultern hoch — und du bemerkst es nicht mehr.",
            "Ausruhen fühlt sich an wie eine Aufgabe, die du auch noch gut machen musst.",
            "Du bist ständig erreichbar. Für alle. Nur bei dir meldet sich niemand.",
            "Fragt dich jemand, was du brauchst, fällt dir nichts ein.",
        ],
        "close": {
            "relief": "Du bist nicht zu empfindlich. Du bist nur zu lange über dich hinweggegangen.",
            "cta": "Speicher dir das — für den Tag, an dem du's wieder vergisst.",
        },
    },
    {
        "slug": "02-nicht-schwach-sondern-nie-aufgehoert",
        "eyebrow": PILLAR_FUNKTION,
        "cover": {
            "hook": "Du bist nicht erschöpft, weil du schwach bist. Sondern weil du nie aufhörst.",
            "sub": "Ein Satz für alle, die immer noch funktionieren.",
        },
        "content": [
            "Du stehst nicht am Limit, weil du zu wenig kannst. Sondern weil du zu lange zu viel getragen hast.",
            "Müde ist nicht das Gegenteil von stark. Müde ist der Preis fürs Durchhalten.",
            "Du hast nie gelernt aufzuhören. Du hast gelernt weiterzumachen — egal, wie es dir ging.",
            "Andere sehen, wie viel du schaffst. Keiner sieht, was es dich kostet.",
            "Aufhören ist kein Versagen. Es ist das Erste, was du dir seit Langem erlaubst.",
        ],
        "close": {
            "relief": "Du musst nicht stärker werden. Du darfst nur endlich leichter werden.",
            "cta": "Wenn dich der Satz trifft: schick ihn einer Frau, die auch nie aufhört.",
        },
    },
    {
        "slug": "03-3-minuten-rueckkehr-atem",
        "eyebrow": PILLAR_YOGA,
        "cover": {
            "hook": "Die 3-Minuten-Rückkehr. Eine Atemübung für Tage, an denen du nur funktionierst.",
            "sub": "Kein Equipment. Kein Können. Nur du und ein Atemzug.",
        },
        "content": [
            "Setz dich hin, wie du gerade bist. Nichts richten, nichts vorbereiten.",
            "Eine Hand auf den Bauch. Spür, wie er sich hebt. Mehr musst du nicht tun.",
            "Atme vier Zählzeiten ein. Lass den Bauch weich werden, nicht die Schultern hoch.",
            "Atme sechs Zählzeiten aus. Länger raus als rein — da fällt die Anspannung ab.",
            "Sechsmal so. Drei Minuten. Mehr braucht dein Körper nicht, um zu merken: du bist da.",
        ],
        "close": {
            "relief": "Du musst nicht runterkommen, um zu funktionieren. Du darfst runterkommen, um wieder bei dir zu sein.",
            "cta": "Speicher dir die Übung — für den nächsten Tag, an dem alles zu schnell wird.",
        },
    },
    {
        "slug": "04-abends-erschoepft-trotz-nichts",
        "eyebrow": PILLAR_FUNKTION,
        "cover": {
            "hook": "Warum du abends erschöpft bist, obwohl du „nichts“ geschafft hast.",
            "sub": "Du hast den ganzen Tag etwas getragen, das niemand sieht.",
        },
        "content": [
            "Du hast nicht „nichts“ gemacht. Du warst nur die ganze Zeit verfügbar.",
            "Mitdenken. Vorausplanen. An das denken, woran sonst keiner denkt. Das zählt nicht als Arbeit — kostet aber genauso viel.",
            "Dein Kopf hatte keine Pause. Auch wenn dein Körper saß.",
            "Erschöpfung kommt nicht nur vom Tun. Sie kommt vom ständigen Bereitsein.",
            "Dass du müde bist, ist kein Beweis, dass du faul warst. Es ist ein Beweis, wie viel du trägst.",
        ],
        "close": {
            "relief": "Du musst dir die Erschöpfung nicht verdienen. Sie ist schon echt.",
            "cta": "Speicher dir das — und lies es abends nochmal, wenn der Zweifel kommt.",
        },
    },
    {
        "slug": "05-3-ruhige-haltungen-abend",
        "eyebrow": PILLAR_YOGA,
        "cover": {
            "hook": "3 ruhige Haltungen für einen Körper, der abends nicht runterkommt.",
            "sub": "Keine Übung zum Können. Eine Einladung zum Loslassen.",
        },
        "content": [
            "Kindhaltung. Knie auseinander, Stirn auf die Matte oder ein Kissen. Hier darfst du dich kurz nicht halten müssen.",
            "Beine hoch an die Wand. Becken nah ran, Arme weit. Der Körper merkt: ich muss gerade nirgends hin.",
            "Liegende Drehung. Knie zur Seite fallen lassen, Blick zur anderen. Du gibst den Tag aus den Schultern ab.",
        ],
        "close": {
            "relief": "Du musst den Tag nicht abarbeiten, um runterzukommen. Manchmal reicht es, dich hinzulegen — und zu bleiben.",
            "cta": "Speicher dir die drei — für den nächsten Abend, der nicht aufhören will.",
        },
    },
    {
        "slug": "06-5-winzige-rueckkehren",
        "eyebrow": PILLAR_YOGA,
        "cover": {
            "hook": "5 winzige Rückkehren. Für Tage, an denen alles zu viel ist.",
            "sub": "Keine Zeit nötig. Nur ein Moment, in dem du dich wieder bemerkst.",
        },
        "content": [
            "Bevor du aufstehst: ein tiefer Atemzug, bei dem die Schultern sinken. Einer reicht.",
            "Beim Zähneputzen: spür die Füße auf dem Boden. Du bist hier, nicht schon im nächsten To-do.",
            "Vor der Tür: kurz stehen bleiben, bevor du losrennst. Drei Sekunden gehören dir.",
            "Mittendrin: die Hand auf den Brustkorb. Frag dich leise — wie geht's mir gerade wirklich?",
            "Abends: eine Hand auf den Bauch, bis der Atem langsamer wird. So sagst du deinem Körper gute Nacht.",
        ],
        "close": {
            "relief": "Du musst nicht erst zur Ruhe kommen, um zurückzufinden. Du findest zurück — in winzigen Momenten.",
            "cta": "Speicher dir die fünf. Und nimm dir heute nur eine vor.",
        },
    },
    {
        "slug": "07-mit-40-nichts-mehr-beweisen",
        "eyebrow": PILLAR_FUNKTION,
        "cover": {
            "hook": "Mit 40+ darfst du aufhören, dich zu beweisen.",
            "sub": "Nicht weil du nichts mehr leisten kannst. Sondern weil du nichts mehr beweisen musst.",
        },
        "content": [
            "Du hast jahrelang funktioniert, um dazuzugehören. Du darfst jetzt einfach da sein.",
            "Du musst nicht die Starke sein, damit man dich braucht. Du darfst gebraucht werden und trotzdem müde sein.",
            "Niemand zieht mehr Bilanz über dein Leben. Außer du selbst — und du darfst milder werden.",
            "Du musst nicht mithalten. Du warst nie im Wettbewerb. Das hat dir nur lange keiner gesagt.",
            "Ab jetzt entscheidest du, wie du leben willst. Nicht, wie du wirken musst.",
        ],
        "close": {
            "relief": "Du wirst nicht weniger, wenn du aufhörst dich zu beweisen. Du kommst zum ersten Mal richtig an.",
            "cta": "Wenn das eine Frau lesen sollte, die du kennst: teil es mit ihr.",
        },
    },
]

HANDLE = "@yoga.statt.funktionieren"

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

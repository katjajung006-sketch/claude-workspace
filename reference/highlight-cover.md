# Highlight-Cover — Design-System

> Instagram Story-Highlight-Cover für @yoga.statt.funktionieren. Einmal festgelegt (2026-06-05), damit neue Cover im gleichen Look entstehen.

## Look (von Katja gewählt)

- **Richtung:** nur Strichsymbol, **kein Wort**.
- **Hintergrund:** Sandbeige `#D8C7B2` (vollflächig — IG stanzt den runden Kreis selbst aus).
- **Symbol:** Espresso `#3A2D28`, schlanke Linie (stroke ~4.6 in 100er-viewBox, runde Enden), mittig zentriert (Kreis-Safe-Zone).
- **Format:** 1080×1920 px. Symbol bewusst klein/zentriert, damit es im runden IG-Ausschnitt sitzt.
- Wirkung als Reihe: ruhig, wie ein Set. Passt zur Karussell-Optik (gleiches Sandbeige).

## Die 7 Highlights → Symbol

| # | Highlight | Symbol |
|---|---|---|
| 1 | Starte hier | Sonnenaufgang |
| 2 | Über mich | Person |
| 3 | Funktionsmodus | Endlos-Schleife |
| 4 | Yoga 40+ | sitzende Figur |
| 5 | 3-Minuten-Yoga | Uhr |
| 6 | Wahre Sätze | Serif-Anführungszeichen (echtes Libre-Baskerville-„“, kein Strich-Icon) |
| 7 | Angebot | Blatt/Zweig |

Reihenfolge = Notion-Datenbank „Story Highlights & Stories". Anführungszeichen ist Text (Libre Baskerville 700), nicht SVG — bleibt nach Canva-Import als Text editierbar.

## Produktion

- **Generator:** `outputs/highlight-covers/gen_final.py` — rendert pro Highlight ein 1080×1920-PNG **und** ein 7-seitiges PDF. HTML/CSS → headless Chrome (`--screenshot` für PNG, `--print-to-pdf` mit `@page{size:1080px 1920px}` für das editierbare PDF). Strichsymbole als Inline-SVG.
- **Output:** `outputs/highlight-covers/final/` — `01-…png` … `07-…png` (direkt in IG hochladbar) + `highlight-cover.pdf`.
- **Vorschau-Sheets** (3 Richtungen als Kreise): `outputs/highlight-covers/vorschau-{A,B,C}.png`.

## Canva-Ablage

- **Design:** „Highlight-Cover — yoga.statt.funktionieren", ID `DAHLvN6rajc` — 7 Seiten, editierbar (Symbole als Bild-Elemente, Anführungszeichen als Text).
  - Edit: https://www.canva.com/d/dzlygrDFLTKmbvj
- **Ordner:** „Highlight-Cover" `FAHLvJtAYGI` (im Bereich „Yoga statt funktionieren").

## Pipeline neues/geändertes Cover

1. In `gen_final.py` `HIGHLIGHTS` + ggf. `icon_svg` anpassen → `python3 gen_final.py`.
2. PDF temporär hosten: Wegwerf-Cloudflare-Projekt (`highlight-import-temp`, **nicht** die Live-Funnel-Projekte), Befehle/Token wie in `reference/cloudflare-config.md` bzw. `secrets.local.md`.
3. `import-design-from-url` (PDF-URL, `intended_design_type = your_story`).
4. `move-item-to-folder` → `FAHLvJtAYGI`.
5. Wegwerf-Projekt löschen, lokales `_host`/`_f_*.html` aufräumen.

## IG-Einsatz

Highlight gedrückt halten → Highlight bearbeiten → Cover bearbeiten → PNG aus `final/` (vorher aufs Handy) oder Canva-Export wählen. IG schneidet den Kreis automatisch aus dem Vollbild.

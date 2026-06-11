# Story-Vorlagen — Design-System

> Editierbares Instagram-Story-Vorlagen-Set für @yoga.statt.funktionieren. Eine Vorlage je Story-Typ. Gebaut 2026-06-11.

## Look
- **Format:** 1080×1920. Marken-Welt: Sandbeige `#D8C7B2`, Creme `#F4EFE7`, Clay `#9A7461`, Espresso `#3A2D28`, Taupe (BTS-Medienfläche) `#C7B49E`.
- **Schrift:** Libre Baskerville (die Sätze) + DM Sans (Eyebrow/Label, CTA, Link).
- **Aufbau je Frame:** kleiner Eyebrow oben (Typ-Name, Clay, gesperrt) + großer ruhiger Text. Viel Luft.

## Die 7 Vorlagen (= Story-Bausteine A–H)
| # | Vorlage | Besonderheit |
|---|---|---|
| 01 | Wahrer Satz | „Vielleicht … Vielleicht …", zentriert, Sandbeige |
| 02 | Spür-Check | Frage + zwei umrandete Options-Boxen (This-or-That-Stand-in) |
| 03 | Mini-Impuls | Moment-Satz + Trennstrich + Übungszeile |
| 04 | Leiser Take | linksbündig, Espresso-Akzentbalken, fett |
| 05 | Frage-Box | offene Frage + umrandete Antwort-Box (IG-Frage-Sticker-Stand-in) |
| 06 | Einladung | Satz + Espresso-CTA-Button + Link (`check.katjajung.com`) |
| 07 | Behind-the-Scenes | Taupe-Medienfläche (für B-Roll) + Creme-Caption-Karte unten |

Texte sind Platzhalter (zeigen Stimme + Stil) — Katja tauscht den Text je Story. Sticker (Slider/Umfrage/Frage) setzt sie in Instagram, nicht in der Vorlage.

## Produktion
- **Generator:** `outputs/story-vorlagen/build.py` — HTML/CSS → headless Chrome. Erzeugt Preview-PNGs (`final/01…07.png`) + ein 7-seitiges PDF (`final/story-vorlagen.pdf`, editierbar in Canva).
- Vorlage ändern: `FRAMES`/`CSS` in `build.py` anpassen → `python3 build.py`.

## Canva-Ablage
- **Design:** „Story-Vorlagen — yoga.statt.funktionieren", ID `DAHMRwHPwjc` — 7 Seiten, editierbar.
  - Edit: https://www.canva.com/d/PpVAATGRyJToH9t
- **Ordner:** „Story-Vorlagen" `FAHMR5OZJJI`.

## Pipeline neue/geänderte Vorlage (wie Highlight-Cover/Karussell)
1. `build.py` anpassen → `python3 build.py`.
2. PDF temporär hosten: Wegwerf-Cloudflare-Projekt `story-import-temp` (Token/Account in `reference/secrets.local.md`; `wrangler pages project create` → `pages deploy _host`). **Nicht** die Live-Funnel-Projekte nutzen.
3. `import-design-from-url` (PDF-URL, `intended_design_type = your_story`).
4. `move-item-to-folder` → `FAHMR5OZJJI`.
5. Temp-Projekt `wrangler pages project delete story-import-temp --yes`, lokales `_host/` löschen.

## Bekannte Import-Tücke
Wie beim Karussell-PDF-Import kann Canva benachbarte Elemente verschmelzen. Mögliche Stellen: die Options-Boxen (02), die Antwort-Box (05) und der CTA-Button (06) könnten als zusammengeführter Block ankommen. Falls ja: in Canva kurz trennen — oder die betroffene Vorlage rein als Text bauen (Boxen/Button weglassen). Reine Text-/Solid-Frames (01, 03, 04, 07) importieren sauber.

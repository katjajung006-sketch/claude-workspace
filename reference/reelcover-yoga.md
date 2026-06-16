# Reelcover-Vorlage — Yoga-Serie

> Einheitliches Cover für die Reels aus `/reel-yoga` + `/reel-yoga-wirkung`. **Neu seit 2026-06-16:** großer Neugier-Hook als Blickfang, „3 MIN" nur als kleines Eck-Badge. Grund: Bei vielen Übungs-Reels las sich das Profil-Grid sonst als Wand aus „3-MINUTEN-ÜBUNG". Der Skill liefert pro Reel nur den Neugier-Hook; das Badge ist fest in der Vorlage.

---

## Look

- **Blickfang:** der **Neugier-Hook**, groß, Libre Baskerville. Trägt den Situations-Anker. 3–6 Wörter, offene Schleife, verrät die Übung nicht.
- **Badge „3 MIN":** klein, mit Uhr-Symbol, DM Sans. **Frei verschiebbar** — Katja zieht es hin, wo sie will (Ecke ihrer Wahl). Ersetzt den alten fixen Kicker „3-MINUTEN-ÜBUNG". Hält die Machbarkeit sichtbar (Kauftrigger Nr. 1), ohne das Grid zu dominieren.
- **Handle:** @yoga.statt.funktionieren, klein, unten.
- **Farben/Schrift:** Sandbeige `#D8C7B2` · Cream `#F4EFE7` · Clay `#9A7461` · Espresso `#3A2D28`. Libre Baskerville (Hook) + DM Sans (Badge/Handle).
- **Format:** 1080×1920.
- **Serien-Wiedererkennung** läuft über den Look (Sandbeige-Welt, Serifenschrift, Badge) — nicht über ein wiederholtes Wort. Foto/Hintergrund bewusst variieren, dann ist auch optisch jede Kachel anders.

## Zwei Varianten (Canva-Vorlage, 2 Seiten)

1. **Foto + Verlauf** (Seite 1): Hintergrund = Standbild der Haltung, dunkler Verlauf unten für Lesbarkeit, Hook + Badge + Handle in Cream.
2. **Einfarbig Sandbeige** (Seite 2): schlichter Sandbeige-Hintergrund, Hook + Handle in Espresso, Badge als Espresso-Pille. Kein Foto nötig.

## Canva-Ablage

- **Design:** „Reelcover-Vorlagen — yoga.statt.funktionieren", ID `DAHMwUMzKLg` — 2 Seiten, editierbar (Hook als Text, Badge als verschiebbares Element).
  - Edit: https://www.canva.com/d/VI-HYlYWyy7HxhT
- **Ordner:** „Reelcover" `FAHMwbZ1N_w`.

## Produktion

- **Generator:** `outputs/reelcover-yoga/build.py` — rendert die zwei Varianten als PNG-Previews + 2-seitiges PDF (HTML/CSS → headless Chrome). Output in `outputs/reelcover-yoga/final/`.
- **Pipeline neue/geänderte Vorlage** (wie Highlight-Cover):
  1. `build.py` anpassen → `python3 build.py`.
  2. PDF temporär hosten: Wegwerf-Cloudflare-Projekt (`reelcover-import-temp`, **nicht** die Live-Funnel-Projekte); Token/Account aus `secrets.local.md`. Erst `wrangler pages project create`, dann `pages deploy`. **Produktions-URL** (`https://<projekt>.pages.dev/<datei>.pdf`) für den Import nehmen — die Preview-Hash-URL wird von Canva nicht zuverlässig geladen.
  3. `import-design-from-url` (PDF-URL, `intended_design_type = your_story`).
  4. `move-item-to-folder` → `FAHMwbZ1N_w`.
  5. Wegwerf-Projekt löschen (`wrangler pages project delete … --yes`), lokales `_host/` aufräumen.

## Workflow pro Reel

1. `/reel-yoga [haltung]` oder `/reel-yoga-wirkung [haltung]` ausführen.
2. Aus dem Output `REELCOVER` den **Neugier-Hook** nehmen.
3. Canva-Design `DAHMwUMzKLg` öffnen, passende Variante (Foto / einfarbig) wählen.
4. Hook-Text ersetzen; bei der Foto-Variante das Haltungs-Foto als Hintergrund einsetzen; Badge bei Bedarf an die gewünschte Ecke schieben.
5. Exportieren (1080×1920) → bei Instagram als Reelcover hochladen.

## Merksatz

Der Neugier-Hook macht neugierig und trägt das Cover. Das „3 MIN"-Badge bleibt klein und beweglich. Variiere Foto/Hintergrund — so wird das Grid abwechslungsreich statt zur Wand aus „3 Minuten".

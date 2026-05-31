#!/usr/bin/env python3
"""Trägt einen kopierten Token sicher in config.json ein — ohne Tippen.

Ablauf:
  1. Token irgendwo kopieren (z.B. mit dem Kopier-Symbol bei Apify/Telegram).
  2. Im Terminal aufrufen, z.B.:
        python3 set_token.py apify_token
        python3 set_token.py telegram_bot_token
        python3 set_token.py telegram_chat_id
  Der Wert wird aus der Zwischenablage (pbpaste) gelesen und gespeichert.
  Der Token wird dabei NICHT im Klartext angezeigt.
"""

import json
import subprocess
import sys
from pathlib import Path

VALID_KEYS = {"apify_token", "telegram_bot_token", "telegram_chat_id"}

if len(sys.argv) != 2 or sys.argv[1] not in VALID_KEYS:
    print("Aufruf: python3 set_token.py <key>")
    print("Erlaubte keys:", ", ".join(sorted(VALID_KEYS)))
    raise SystemExit(1)

key = sys.argv[1]

try:
    value = subprocess.check_output(["pbpaste"]).decode("utf-8").strip()
except Exception as e:
    print("Konnte Zwischenablage nicht lesen:", e)
    raise SystemExit(1)

if not value:
    print("Zwischenablage ist leer. Bitte zuerst den Token kopieren.")
    raise SystemExit(1)

cfg_path = Path(__file__).resolve().parent / "config.json"
cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
cfg[key] = value
cfg_path.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

masked = value[:4] + "…" + value[-4:] if len(value) > 8 else "(gesetzt)"
print(f"✓ {key} gespeichert ({masked}). Länge: {len(value)} Zeichen.")

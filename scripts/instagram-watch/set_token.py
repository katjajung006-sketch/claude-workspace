#!/usr/bin/env python3
"""Trägt einen Token sicher in config.json ein.

Ablauf:
  1. Im Terminal aufrufen, z.B.:
        python3 set_token.py apify_token
        python3 set_token.py telegram_bot_token
  2. Das Skript fragt nach dem Wert — Token einfügen und Enter drücken.
"""

import json
import sys
from pathlib import Path

VALID_KEYS = {"apify_token", "telegram_bot_token", "telegram_chat_id"}

if len(sys.argv) != 2 or sys.argv[1] not in VALID_KEYS:
    print("Aufruf: python3 set_token.py <key>")
    print("Erlaubte keys:", ", ".join(sorted(VALID_KEYS)))
    raise SystemExit(1)

key = sys.argv[1]

# Immer interaktiv fragen — am einfachsten und ohne Zwischenablage-Stolperfallen.
print(f"Füge den Wert für '{key}' ein und drück Enter:")
value = input("> ").strip()

if not value or any(ch.isspace() for ch in value) or value.startswith(("python3", "cd ", "HIER_")):
    print("Das sieht nicht nach einem gültigen Token aus. Bitte nochmal versuchen.")
    raise SystemExit(1)

cfg_path = Path(__file__).resolve().parent / "config.json"
cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
cfg[key] = value
cfg_path.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

masked = value[:4] + "…" + value[-4:] if len(value) > 8 else "(gesetzt)"
print(f"✓ {key} gespeichert ({masked}). Länge: {len(value)} Zeichen.")

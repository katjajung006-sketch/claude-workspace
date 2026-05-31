#!/usr/bin/env python3
"""Findet deine Telegram chat_id.

So geht's:
1. Bot bei @BotFather erstellen, Token in config.json eintragen.
2. In Telegram deinem neuen Bot eine beliebige Nachricht schicken (z.B. "hallo").
3. Dieses Skript ausführen:  python3 get_chat_id.py
4. Die angezeigte chat_id in config.json eintragen.
"""

import json
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
cfg = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
token = cfg.get("telegram_bot_token", "").strip()

if not token or token.startswith("HIER_"):
    print("Bitte zuerst telegram_bot_token in config.json eintragen.")
    raise SystemExit(1)

url = f"https://api.telegram.org/bot{token}/getUpdates"
with urllib.request.urlopen(url, timeout=30) as r:
    data = json.load(r)

if not data.get("ok"):
    print("Telegram-Antwort nicht ok:", data)
    raise SystemExit(1)

results = data.get("result", [])
if not results:
    print("Keine Nachrichten gefunden. Schick deinem Bot zuerst eine Nachricht in Telegram,")
    print("dann dieses Skript erneut ausführen.")
    raise SystemExit(0)

seen = {}
for upd in results:
    msg = upd.get("message") or upd.get("edited_message") or {}
    chat = msg.get("chat", {})
    if chat.get("id"):
        name = chat.get("first_name") or chat.get("title") or chat.get("username") or "?"
        seen[chat["id"]] = name

print("Gefundene chat_id(s):")
for cid, name in seen.items():
    print(f"  {cid}   ({name})")
print("\nTrage die passende Zahl als telegram_chat_id in config.json ein.")

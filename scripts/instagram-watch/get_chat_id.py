#!/usr/bin/env python3
"""Findet deine Telegram chat_id und trägt sie automatisch in config.json ein.

So geht's:
1. Bot bei @BotFather erstellen, Token mit set_token.py speichern.
2. In Telegram deinem neuen Bot eine beliebige Nachricht schicken (z.B. "hallo").
3. Dieses Skript ausführen:  python3 get_chat_id.py
   -> Bei genau einem Chat wird die chat_id direkt gespeichert.
   -> Bei mehreren: erneut mit der gewünschten Nummer aufrufen,
      z.B.  python3 get_chat_id.py 123456789
"""

import json
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CFG_PATH = HERE / "config.json"
cfg = json.loads(CFG_PATH.read_text(encoding="utf-8"))
token = cfg.get("telegram_bot_token", "").strip()

if not token or token.startswith("HIER_"):
    print("Bitte zuerst telegram_bot_token speichern:")
    print("  python3 set_token.py telegram_bot_token")
    raise SystemExit(1)


def save_chat_id(cid):
    cfg["telegram_chat_id"] = str(cid)
    CFG_PATH.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"✓ telegram_chat_id gespeichert: {cid}")
    print("Fertig! Jetzt kannst du den Testlauf machen:  python3 watch.py")


# Falls die chat_id direkt als Argument übergeben wird
if len(sys.argv) == 2:
    save_chat_id(sys.argv[1].strip())
    raise SystemExit(0)

url = f"https://api.telegram.org/bot{token}/getUpdates"
with urllib.request.urlopen(url, timeout=30) as r:
    data = json.load(r)

if not data.get("ok"):
    print("Telegram-Antwort nicht ok:", data)
    raise SystemExit(1)

results = data.get("result", [])
if not results:
    print("Keine Nachrichten gefunden.")
    print("Schick deinem Bot zuerst eine Nachricht in Telegram (z.B. 'hallo'),")
    print("dann dieses Skript erneut ausführen.")
    raise SystemExit(0)

seen = {}
for upd in results:
    msg = upd.get("message") or upd.get("edited_message") or {}
    chat = msg.get("chat", {})
    if chat.get("id"):
        name = chat.get("first_name") or chat.get("title") or chat.get("username") or "?"
        seen[chat["id"]] = name

if len(seen) == 1:
    cid = next(iter(seen))
    save_chat_id(cid)
else:
    print("Mehrere Chats gefunden:")
    for cid, name in seen.items():
        print(f"  {cid}   ({name})")
    print("\nRuf das Skript erneut mit der passenden Nummer auf, z.B.:")
    print(f"  python3 get_chat_id.py {next(iter(seen))}")

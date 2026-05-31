#!/bin/bash
# Wrapper für den täglichen launchd-Lauf.
# Setzt einen PATH, in dem sowohl python3 als auch das Claude Code CLI gefunden werden.
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin"
cd "$(dirname "$0")" || exit 1
/usr/bin/python3 watch.py >> watch.log 2>&1

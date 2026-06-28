# Cloudflare Pages — Deploy-Konfiguration

Hosting der statischen Funnel-Seiten. Ersetzt Netlify (dort wurde das Konto wegen Credit-Limit pausiert).

## Zugangsdaten

Die echten Werte stehen in `reference/secrets.local.md` (gitignored, wird nie ins Repo gepusht).
Vor dem Deploy als Umgebungsvariablen setzen — siehe dort.

- API Token: Scope Pages:Edit — Wert in `secrets.local.md`
- Account ID — Wert in `secrets.local.md`

Token kann jederzeit im Cloudflare-Dashboard (My Profile → API Tokens) widerrufen/neu erstellt werden.

## Zwei Pages-Projekte

| Projekt | Ordner | Custom Domain | pages.dev |
| --- | --- | --- | --- |
| `katjajung-check` | `cloudflare-deploy/check/` | check.katjajung.com | katjajung-check.pages.dev |
| `kurs-10-minuten-rueckkehr` | `cloudflare-deploy/kurs/` | 10-minuten-rueckkehr.katjajung.com | kurs-10-minuten-rueckkehr.pages.dev |
| `katjajung-start` | `cloudflare-deploy/start/` | start.katjajung.com | katjajung-start.pages.dev |

**Projekt 1 (check):** index.html (Landingpage), angebot.html (€7-Tripwire-Verkaufsseite), optin.html, katja.jpg
**Projekt 2 (kurs):** index.html (= die öffentliche €17-Kursseite, ursprünglich kurs.html)
**Projekt 3 (start):** index.html (= der Instagram-Bio-Link-Hub, Quelle `website-quelle/start.html`), katja.jpg. Ersetzt Linktree als zweiten Bio-Link. Neue Miniprodukte = einfach als weitere Karte in `website-quelle/start.html` ergänzen und neu deployen — die Bio bleibt unverändert.

Hinweis: Cloudflare Pages nutzt „Clean URLs" — `/angebot.html` leitet per 308 auf `/angebot`. Beides liefert 200. Kein host-basierter `_redirects`-Trick nötig (deshalb zwei Projekte statt einem).

## Deploy-Befehle

Quelle bleibt `website-quelle/` (früher `netlify-deploy/` — umbenannt 2026-06-22). Vor dem Deploy die Ordner synchronisieren:

```bash
cd /Users/katjajung/claude-workspace-vorlage
cp website-quelle/index.html website-quelle/angebot.html website-quelle/optin.html website-quelle/katja.jpg cloudflare-deploy/check/
cp website-quelle/kurs.html cloudflare-deploy/kurs/index.html

# Token + Account-ID aus reference/secrets.local.md setzen (gitignored):
export CLOUDFLARE_API_TOKEN=<siehe secrets.local.md>
export CLOUDFLARE_ACCOUNT_ID=<siehe secrets.local.md>

npx --yes wrangler@latest pages deploy cloudflare-deploy/check --project-name=katjajung-check --branch=main --commit-dirty=true
npx --yes wrangler@latest pages deploy cloudflare-deploy/kurs --project-name=kurs-10-minuten-rueckkehr --branch=main --commit-dirty=true

# Bio-Link-Hub (vor Deploy synchronisieren):
cp website-quelle/start.html cloudflare-deploy/start/index.html
cp website-quelle/katja.jpg cloudflare-deploy/start/katja.jpg
npx --yes wrangler@latest pages deploy cloudflare-deploy/start --project-name=katjajung-start --branch=main --commit-dirty=true
```

Hinweis: Das Projekt `katjajung-start` wurde am 2026-06-28 neu angelegt (`wrangler pages project create katjajung-start --production-branch=main`, dann Custom Domain via API: `POST /accounts/{id}/pages/projects/katjajung-start/domains` mit `{"name":"start.katjajung.com"}`).

## DNS bei One.com (CNAME)

| Host | Ziel |
| --- | --- |
| `check` | `katjajung-check.pages.dev` |
| `10-minuten-rueckkehr` | `kurs-10-minuten-rueckkehr.pages.dev` |
| `start` | `katjajung-start.pages.dev` |

Alte Netlify-Ziele (`celebrated-wisp-6ee073.netlify.app`) ersetzen. SSL stellt Cloudflare nach DNS-Verifizierung automatisch aus.

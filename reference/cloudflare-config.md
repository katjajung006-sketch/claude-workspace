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

**Projekt 1 (check):** index.html (Landingpage), angebot.html (€7-Tripwire-Verkaufsseite), optin.html, katja.jpg
**Projekt 2 (kurs):** index.html (= die öffentliche €17-Kursseite, ursprünglich kurs.html)

Hinweis: Cloudflare Pages nutzt „Clean URLs" — `/angebot.html` leitet per 308 auf `/angebot`. Beides liefert 200. Kein host-basierter `_redirects`-Trick nötig (deshalb zwei Projekte statt einem).

## Deploy-Befehle

Quelle bleibt `netlify-deploy/`. Vor dem Deploy die Ordner synchronisieren:

```bash
cd /Users/katjajung/Desktop/claude-workspace-vorlage
cp netlify-deploy/index.html netlify-deploy/angebot.html netlify-deploy/optin.html netlify-deploy/katja.jpg cloudflare-deploy/check/
cp netlify-deploy/kurs.html cloudflare-deploy/kurs/index.html

# Token + Account-ID aus reference/secrets.local.md setzen (gitignored):
export CLOUDFLARE_API_TOKEN=<siehe secrets.local.md>
export CLOUDFLARE_ACCOUNT_ID=<siehe secrets.local.md>

npx --yes wrangler@latest pages deploy cloudflare-deploy/check --project-name=katjajung-check --branch=main --commit-dirty=true
npx --yes wrangler@latest pages deploy cloudflare-deploy/kurs --project-name=kurs-10-minuten-rueckkehr --branch=main --commit-dirty=true
```

## DNS bei One.com (CNAME)

| Host | Ziel |
| --- | --- |
| `check` | `katjajung-check.pages.dev` |
| `10-minuten-rueckkehr` | `kurs-10-minuten-rueckkehr.pages.dev` |

Alte Netlify-Ziele (`celebrated-wisp-6ee073.netlify.app`) ersetzen. SSL stellt Cloudflare nach DNS-Verifizierung automatisch aus.

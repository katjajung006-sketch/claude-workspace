# Netlify Deploy-Konfiguration (VERALTET)

> Hosting ist zu **Cloudflare Pages** umgezogen (Netlify-Konto wegen Credit-Limit pausiert).
> Siehe `reference/cloudflare-config.md`. Diese Datei nur noch zur Referenz.

**Site:** check.katjajung.com
**Site ID:** 1a07544c-cfb6-4c63-988c-27a2b3db4cf6
**Token:** in `reference/secrets.local.md` (gitignored) — sollte im Netlify-Dashboard widerrufen werden, wird nicht mehr gebraucht.

## Deploy-Befehl (nicht mehr aktiv)

```bash
cd /Users/katjajung/Desktop/claude-workspace-vorlage/netlify-deploy && \
zip -r /tmp/netlify-deploy.zip . && \
curl -s -X POST \
  -H "Authorization: Bearer <TOKEN aus secrets.local.md>" \
  -H "Content-Type: application/zip" \
  --data-binary @/tmp/netlify-deploy.zip \
  "https://api.netlify.com/api/v1/sites/1a07544c-cfb6-4c63-988c-27a2b3db4cf6/deploys"
```

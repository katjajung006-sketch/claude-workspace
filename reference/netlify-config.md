# Netlify Deploy-Konfiguration

**Site:** check.katjajung.com  
**Site ID:** 1a07544c-cfb6-4c63-988c-27a2b3db4cf6  
**Token:** nfp_jXtGQyXRonZuYoTWbiAB7pnbVLPPtcia41df

## Deploy-Befehl

```bash
cd /Users/katjajung/Desktop/claude-workspace-vorlage/netlify-deploy && \
zip -r /tmp/netlify-deploy.zip . && \
curl -s -X POST \
  -H "Authorization: Bearer nfp_jXtGQyXRonZuYoTWbiAB7pnbVLPPtcia41df" \
  -H "Content-Type: application/zip" \
  --data-binary @/tmp/netlify-deploy.zip \
  "https://api.netlify.com/api/v1/sites/1a07544c-cfb6-4c63-988c-27a2b3db4cf6/deploys"
```

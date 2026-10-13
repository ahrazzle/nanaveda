Run the real browser regression journeys with optional Playwright tooling:

```sh
npm install --no-save --package-lock=false playwright
npx playwright install chromium
node tests/browser.mjs
```

The script starts an ephemeral local HTTP server, checks recipe history, glossary failure, modal keyboard/focus behavior and persisted text size, then closes the browser/server. It makes no provider calls. `PLAYWRIGHT_MODULE` can point to an already installed Playwright module.

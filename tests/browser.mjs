import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { resolve, extname } from 'node:path';
import assert from 'node:assert/strict';
const { chromium } = await import(process.env.PLAYWRIGHT_MODULE || 'playwright');
const root = resolve(fileURLToPath(new URL('../', import.meta.url)));
const types = {'.html':'text/html','.js':'text/javascript','.json':'application/json','.css':'text/css','.svg':'image/svg+xml','.jpg':'image/jpeg'};
const server = createServer(async (req,res) => {
  try {
    let path = resolve(root, '.' + new URL(req.url, 'http://test').pathname);
    if (!path.startsWith(root)) throw new Error('Invalid path');
    if ((await stat(path)).isDirectory()) path += '/index.html';
    res.setHeader('content-type', types[extname(path)] || 'application/octet-stream');
    res.end(await readFile(path));
  } catch { res.writeHead(404).end(); }
});
await new Promise(resolve => server.listen(0,'127.0.0.1',resolve));
const url = `http://127.0.0.1:${server.address().port}`;
const browser = await chromium.launch({headless:true});
try {
  const page = await browser.newPage({viewport:{width:390,height:844}});
  const errors=[]; page.on('pageerror',e=>errors.push(String(e)));
  await page.route('https://en.wikipedia.org/**', route => route.abort());
  await page.goto(url+'/#page-recipe-1');
  await page.waitForSelector('.term[tabindex]');
  await page.waitForFunction(()=>Object.keys(termsDB).length > 0);
  const term=page.locator('.page-view.active .term').first();
  await term.focus(); await page.keyboard.press('Space');
  await page.waitForSelector('#term-popup.active');
  assert.equal(await page.locator('.page-view.active').getAttribute('id'),'page-recipe-1');
  await page.locator('.term-popup-close').click();
  assert.equal(await term.evaluate(e=>e===document.activeElement),true);
  await term.click();await page.keyboard.press('Tab');
  assert.equal(await page.evaluate(()=>!!document.activeElement.closest('#term-popup')),true);
  await page.keyboard.press('Escape');
  await page.locator('#nextBtn').click();
  assert.equal(await page.locator('.page-view.active').getAttribute('id'),'page-recipe-2');
  await page.goBack();
  assert.equal(await page.locator('.page-view.active').getAttribute('id'),'page-recipe-1');
  await page.locator('#ts-large').click();await page.reload();
  assert.equal(await page.locator('#ts-large').evaluate(e=>e.classList.contains('active')),true);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  // A glossary miss must finish in an error state, never stay loading forever.
  await page.evaluate(()=>openTermPopup('unavailable_test_term',{preventDefault(){},stopPropagation(){}}));
  assert.match(await page.locator('.term-popup-description').innerText(),/Definition unavailable/);
  assert.deepEqual(errors,[]);
  console.log('Recipe history, keyboard/modal focus, text size, glossary failure and mobile width pass.');
} finally { await browser.close(); await new Promise(resolve=>server.close(resolve)); }

"""Optional integration test suite: pip install playwright; playwright install chromium.
Run: python tests/smoke_test.py
Works without internet once browser binaries are installed.
"""
import asyncio
import shutil
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True, **({"executable_path":shutil.which("chromium")} if shutil.which("chromium") else {}))
        page=await browser.new_page(viewport={"width":1280,"height":800})
        errors=[]
        page.on('pageerror',lambda err:errors.append(str(err)))
        await page.set_content((ROOT/'index.html').read_text(encoding='utf-8'),wait_until='domcontentloaded')
        assert await page.locator('#homeKpis .kpi-card').count()==4
        assert '34' in await page.locator('#homeKpis').inner_text()
        await page.locator('[data-page="unicode"]').click()
        await page.locator('#loadUnicodeDemo').click()
        text=await page.locator('#decodedMessages').inner_text()
        assert 'SIGNALFORGE' in text and 'meet at midnight' in text,text
        await page.locator('[data-page="forge"]').click()
        assert '960×540' in await page.locator('#renderTiming').inner_text()
        await page.locator('#benchSignal').click()
        await page.locator('#signalBench tbody tr').first.wait_for(timeout=20000)
        assert await page.locator('#signalBench tbody tr').count()==3
        await page.locator('[data-page="archive"]').click()
        assert await page.locator('#archiveGrid .sample-tile').count()==34
        await page.set_viewport_size({"width":390,"height":844})
        await page.locator('[data-page="unicode"]').click()
        width=await page.evaluate('document.documentElement.scrollWidth')
        assert width==390,f'Horizontal overflow: {width}'
        assert not errors,errors
        print('PASS: archive, Unicode VS+INV1 decoding, pixel forge, compression, responsive UI.')
        await browser.close()
asyncio.run(main())

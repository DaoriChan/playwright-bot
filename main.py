import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # headless=False для видимости
        page = await browser.new_page()
        await page.goto("https://cerebrysquad.xyz")
        print("Opened cerebrysquad!")

        while True:
            print("still alive")
            await asyncio.sleep(5)

asyncio.run(main())

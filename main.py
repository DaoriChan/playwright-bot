import asyncio
from playwright.async_api import async_playwright

async def main():
    print("Запускаем Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://cerebrysquad.github.io/")
        print("Страница загружена!")
      

asyncio.run(main())

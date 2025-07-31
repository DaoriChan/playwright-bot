import asyncio
from playwright.async_api import async_playwright

async def visit_site():
    print("Запуск Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            await page.goto("https://cerebrysquad.github.io/")
            title = await page.title()
            print(f"Сайт загружен\nЗаголовок страницы: {title}")
        except Exception as e:
            print("Ошибка:", e)
        await browser.close()

async def keep_alive():
    while True:
        print("Бот работает...")
        await asyncio.sleep(5)

async def main():
    await visit_site()
    await keep_alive()

asyncio.run(main())

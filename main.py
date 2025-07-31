import asyncio
from playwright.async_api import async_playwright

async def main():
    print("Запускаем Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://cerebrysquad.github.io/")
        print("Страница загружена!")

        # 10 итераций ожидания
        for i in range(10):
            print(f"[{(i+1)*5} сек] Still alive...")
            await asyncio.sleep(5)

        print("10 итераций завершены. Завершаем скрипт.")
        await browser.close()

asyncio.run(main())

import asyncio
from playwright.async_api import async_playwright

async def main():
    print("Запускаем Playwright...", flush=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://cerebrysquad.github.io/")
        print("Страница загружена!", flush=True)

        # 10 итераций ожидания
        for i in range(10):
            print(f"[{(i+1)*5} сек] Still alive...", flush=True)
            await asyncio.sleep(5)

        print("10 итераций завершены. Завершаем скрипт.", flush=True)
        await browser.close()
        print("БУМ! 💥", flush=True)

asyncio.run(main())

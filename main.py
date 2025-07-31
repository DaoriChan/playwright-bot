from playwright.sync_api import sync_playwright

def check():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Пример: логин
        page.goto("https://example.com/login")
        page.fill('input[name="username"]', "ТВОЙ_ЛОГИН")
        page.fill('input[name="password"]', "ТВОЙ_ПАРОЛЬ")
        page.click('button[type="submit"]')

        page.wait_for_load_state("networkidle")
        page.goto("https://example.com/protected_page")
        
        html = page.content()
        print("✓ Получена страница, длина:", len(html))
        browser.close()

if __name__ == "__main__":
    check()

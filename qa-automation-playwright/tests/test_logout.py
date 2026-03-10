import time
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login
        login_page = LoginPage(page)
        login_page.go_to_login()
        time.sleep(1)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(1)

        # Logout
        home_page = HomePage(page)
        home_page.logout()
        time.sleep(1)

        # Verifica se voltou para login
        assert page.url == "https://www.saucedemo.com/"
        time.sleep(2)

        browser.close()
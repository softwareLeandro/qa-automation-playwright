import time
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

# Teste positivo: login correto
def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # navegador visível
        page = browser.new_page()
        login_page = LoginPage(page)
        login_page.go_to_login()
        time.sleep(1)  # esperar página carregar
        login_page.login("standard_user", "secret_sauce")
        time.sleep(1)  # esperar login processar
        assert login_page.is_logged_in()
        time.sleep(2)  # visualizar página final antes de fechar
        browser.close()

# Teste negativo: login incorreto
def test_login_invalid():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        login_page.go_to_login()
        time.sleep(1)
        login_page.login("invalid_user", "wrong_password")
        time.sleep(1)
        error = login_page.get_error_message()
        assert "Username and password do not match any user" in error
        time.sleep(2)
        browser.close()
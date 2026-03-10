# tests/test_cart.py
import time
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login
        login_page = LoginPage(page)
        login_page.go_to_login()
        time.sleep(1)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(1)

        # Adicionar produto
        product_page = ProductsPage(page)
        product_page.add_to_cart_backpack()
        time.sleep(1)

        # Verificar carrinho
        assert product_page.cart_count() == 1
        time.sleep(2)

        browser.close()
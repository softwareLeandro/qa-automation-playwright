# pages/products_page.py
from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = ".shopping_cart_badge"

    def add_to_cart_backpack(self):
        # botão real do SauceDemo
        self.page.click("#add-to-cart-sauce-labs-backpack")

    def cart_count(self):
        if self.page.is_visible(self.cart_badge):
            return int(self.page.inner_text(self.cart_badge))
        return 0
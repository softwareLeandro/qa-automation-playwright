# pages/home_page.py
class HomePage:
    def __init__(self, page):
        self.page = page
        self.menu_button = "#react-burger-menu-btn"
        self.logout_link = "#logout_sidebar_link"

    def logout(self):
        self.page.click(self.menu_button)
        self.page.click(self.logout_link)
import pytest
from playwright.sync_api import Page, expect

class LogoutPage:
    def __init__(self,page:Page):
        self.page=page

        self.logout = self.page.locator("a").filter(has_text="Logout").first()


    def click_logout(self):
        self.logout.wait_for(state="visible", timeout=5000)
        self.logout.click()
        
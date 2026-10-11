from playwright.sync_api import Page
import re

class Homepage:
    def __init__(self, page: Page):
        """
        Constructor to initialize Playwright page object & define all necessary locators.
        """
        self.page = page

        # -------------Locators-----------------#
        self.link_my_account = self.page.get_by_title('My Account')
        
        # ✅ FIX 1: Changed colons (:) to equals signs (=) for proper keyword arguments
        self.link_register = self.page.get_by_role('link', name='Register')
        self.link_login = self.page.get_by_role('link', name='Login')
        
        self.search_box = self.page.get_by_placeholder("Search")
        self.search_btn = self.page.locator("button.btn.btn-default.btn-lg:visible") 

    def click_my_account(self):
        self.link_my_account.wait_for(state="visible", timeout=20000)
        self.link_my_account.click()

    def click_link_register(self):
        self.link_register.wait_for(state="visible", timeout=20000)
        self.link_register.click()

    def click_link_login(self):
        self.link_login.click()

    def click_search_box(self, product_name: str):
        self.search_box.fill(product_name)

    def click_search_btn(self):
        self.search_btn.click()

        
        
            
            
            


       
       

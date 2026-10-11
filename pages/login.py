import pytest
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self,page:Page):
        self.page=page

        self.email_input = self.page.get_by_placeholder("E-Mail Address")
        self.password_input = self.page.get_by_placeholder("Password")
        self.login_btn = self.page.locator("input.btn.btn-primary")


    def enter_email(self,email:str):
        self.email_input.fill(email)

    def enter_password(self,password:str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_btn.click()

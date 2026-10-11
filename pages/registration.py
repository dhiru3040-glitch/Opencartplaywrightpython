import pytest
from playwright.sync_api import Page, expect

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
    
    # ===== Locators =====
    # Input fields
        self.txt_firstname = self.page.locator('#input-firstname')
        self.txt_lastname = self.page.locator('#input-lastname')
        self.txt_email = self.page.locator('#input-email')
        self.txt_telephone = self.page.locator('#input-telephone')
        self.txt_password = self.page.locator('#input-password')
        self.txt_confirm_password = self.page.locator('#input-confirm')
    
    # Checkbox and buttons
        self.chk_policy = self.page.locator('input[name="agree"]')
        self.btn_continue = self.page.locator('input[value="Continue"]')
    
    # Confirmation message (displayed after successful registration)
        self.msg_confirmation = self.page.locator('h1:has-text("Your Account Has Been Created!")')

    def enter_first_name(self,fname:str):
        self.txt_firstname.fill(fname)

    def enter_last_name(self,lname:str):
        self.txt_lastname.fill(lname)

    def enter_email(self,email:str):
        self.txt_email.fill(email)

    def enter_telephone(self,num:str):
        self.txt_telephone.fill(num)

    def enter_password(self,password:str):
        self.txt_password.fill(password)

    def enter_con_password(self,conpass:str):
        self.txt_confirm_password.fill(conpass)

    def click_checkbox(self):
        self.chk_policy.check()

    def click_continue(self):
        self.btn_continue.wait_for(state="visible", timeout=20000)
        self.btn_continue.evaluate("node => node.click()")

    def get_confirmation_msg(self):
        self.msg_confirmation.wait_for(state="visible", timeout=20000)
        return self.msg_confirmation

    
    

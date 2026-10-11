import pytest
from playwright.sync_api import Page, expect
from pages.homepage import Homepage
from pages.registration import RegistrationPage
from pages.login import LoginPage
from pages.logout import LogoutPage
from Utils.random_data_util import RandomDataUtil

def test_end_to_end_flow(page):
    page.goto('.')
    page.wait_for_load_state('domcontentloaded')

    home_page = Homepage(page)
    registration_page = RegistrationPage(page)
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)
    random_data = RandomDataUtil(page)

    # User Registration
    
    home_page.click_my_account()
    home_page.click_link_register()
    

        # 🔐 FIX: Store both unique data strings in memory first
    generated_password = random_data.get_password()
    generated_email = random_data.get_email()

    registration_page.enter_first_name(random_data.get_first_name())
    registration_page.enter_last_name(random_data.get_last_name())
    registration_page.enter_email(generated_email)
    registration_page.enter_telephone(random_data.get_phone_number())
    registration_page.enter_password(generated_password)
    registration_page.enter_con_password(generated_password)

    registration_page.click_checkbox()
    registration_page.click_continue()

    confirmation_msg = registration_page.get_confirmation_msg()
    expect(confirmation_msg).to_have_text("Your Account Has Been Created!")
    home_page.click_my_account()
    home_page.click_link_register()
    

    registration_page.enter_first_name(random_data.get_first_name())
    registration_page.enter_last_name(random_data.get_last_name())
    registration_page.enter_email(generated_email)
    registration_page.enter_telephone(random_data.get_phone_number())
    registration_page.enter_password(generated_password)
    registration_page.enter_con_password(generated_password)

    registration_page.click_checkbox()
    registration_page.click_continue()

    confirmation_msg = registration_page.get_confirmation_msg()
    expect(confirmation_msg).to_have_text("Your Account Has Been Created!")

    # Logout after registration
    home_page.click_my_account()
    logout_page.click_logout()

    # Login with the newly registered user
    home_page.click_my_account()
    home_page.click_link_login()

    login_page.enter_email(generated_email)
    login_page.enter_password(generated_password)
    login_page.click_login()

    # Verify successful login by checking for a specific element or message
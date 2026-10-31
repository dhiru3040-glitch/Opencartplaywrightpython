
import pytest
from playwright.sync_api import Page, expect

from pages.homepage import Homepage
from pages.registration import RegistrationPage
from Utils.random_data_util import RandomDataUtil

@pytest.mark.sanity
def test_user_registration(page):
    page.goto('.')
    page.wait_for_load_state('domcontentloaded')
    home_page=Homepage(page)
    registration_page= RegistrationPage(page)

    home_page.click_my_account()
    home_page.click_link_register()

    random_data= RandomDataUtil(page)

     # 🔐 Capture the password inside a variable first!
    generated_password = random_data.get_password()

    registration_page.enter_first_name(random_data.get_first_name())
    registration_page.enter_last_name(random_data.get_last_name())
    registration_page.enter_email(random_data.get_email())
    registration_page.enter_telephone(random_data.get_phone_number())
    registration_page.enter_password(generated_password)
    registration_page.enter_con_password(generated_password)

    registration_page.click_checkbox()
    registration_page.click_continue()

    confirmation_msg = registration_page.get_confirmation_msg()
    expect(confirmation_msg).to_have_text("Your Account Has Been Created!")
    print("test case passed")
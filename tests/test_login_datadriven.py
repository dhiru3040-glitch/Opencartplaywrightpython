from pages.homepage import Homepage
from pages.login import LoginPage
from playwright.sync_api import expect
from Utils.data_reader import read_excel_data
import pytest
excel_data = read_excel_data('testdata/logindata.xlsx', 'Sheet1')


@pytest.mark.sanity
@pytest.mark.parametrize("testname, email, password, expected", excel_data)
def test_login_datadriven(page,testname, email, password, expected):
    page.goto('.')
    page.wait_for_load_state('domcontentloaded')
    home_page = Homepage(page)
    login_page = LoginPage(page)

    home_page.click_my_account()
    home_page.click_link_login()

    

    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login()

    page.wait_for_timeout(5000)  # Wait for 2 seconds to allow the page to load after 

    
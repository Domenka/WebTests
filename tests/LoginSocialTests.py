import allure

from core.BaseTest import browser
from pages.BasePageHelper import BasePageHelper
from pages.LoginSocialPage import LoginSocialHelper

BASE_URL = "https://sn.rv-school.ru"

def test_empty_login_and_password(browser):
    with allure.step("Открытие страницы"):
        BasePageHelper(browser).driver.get(BASE_URL)

    login_page = LoginSocialHelper(browser)
    login_page.click_registration_button
    login_page.click_register_by_phone_button
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from faker import Faker
from page_texts.PageTexts import PageTexts

BASE_URL = "https://ok.ru/"


def test_empty_login_and_password(browser):
    BasePage(browser).driver.get(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.login_click()
    assert LoginPage.get_error_login_text() == PageTexts.EMPTY_LOGIN_ERROR.value

def test_login_without_password(browser):
    faker = Faker()
    BasePage(browser).driver.get(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.set_login(text=faker.name())
    LoginPage.login_click()
    assert LoginPage.get_error_password_text() == PageTexts.EMPTY_PASSWORD_ERROR.value

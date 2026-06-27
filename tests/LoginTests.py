import allure

from core.BaseTest import browser
from pages.BasePageHelper import BasePageHelper
from pages.LoginPage import LoginPageHelper
from faker import Faker
from page_texts.PageTexts import PageTexts

BASE_URL = "https://ok.ru/"

@allure.suite("Тестирование формы авторизации")
@allure.title("Проверка наличия текста ошибки при логине с пустыми кредами")
def test_empty_login_and_password(browser):
    with allure.step("Открытие страницы"):
        BasePageHelper(browser).driver.get(BASE_URL)

    login_page = LoginPageHelper(browser)
    login_page.login_click()

    with allure.step("Проверка соответствия текста ошибки"):
        assert login_page.get_error_login_text() == PageTexts.EMPTY_LOGIN_ERROR.value

@allure.suite("Тестирование формы авторизации")
@allure.title("Проверка наличия текста ошибки при логине с пустым паролем")
def test_login_without_password(browser):
    faker = Faker()
    with allure.step("Открытие страницы"):
        BasePageHelper(browser).driver.get(BASE_URL)

    LoginPage = LoginPageHelper(browser)
    LoginPage.set_login(text=faker.name())
    LoginPage.login_click()

    with allure.step("Проверка соответствия текста ошибки"):
        assert LoginPage.get_error_password_text() == PageTexts.EMPTY_PASSWORD_ERROR.value
import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from faker import Faker
from page_texts.PageTexts import PageTexts
from pages.RecoveryPage import RecoveryPageHelper

BASE_URL = "https://ok.ru/"

@allure.suite("Тестирование формы восстановления доступа")
@allure.title("Проверка перехода к форме восстановления после нескольких неудачных попыток авторизоваться")
def test_transfer_to_recovery_page(browser):
    with allure.step("Открытие страницы авторизации"):
        faker = Faker()
        BasePage(browser).driver.get(BASE_URL)

        LoginPage = LoginPageHelper(browser)
        LoginPage.set_login(text=faker.name())
        LoginPage.set_wrong_password("1")

        for i in range(3):
            LoginPage.set_wrong_password("1")
            LoginPage.login_click()

        LoginPage.click_recovery()
        RecoveryPage = RecoveryPageHelper(browser)
        RecoveryPage.check_page()



import allure

from core.BaseTest import browser
from pages.BasePageHelper import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VKEcosystemPage import VKEcosystemHelper

BASE_URL = "https://ok.ru/"

@allure.suite("Проверка тулбара")
@allure.title("Переход к экосистемам ВКонтакте")
def test_open_ecosystem(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    current_window = LoginPage.get_windows_id(0)
    LoginPage.click_vk_ecosystems()
    LoginPage.click_more_services()
    new_window = LoginPage.get_windows_id(1)
    LoginPage.switch_window(new_window)
    VKEcosystemPage = VKEcosystemHelper(browser)
    VKEcosystemPage.switch_window(current_window)
    LoginPageHelper(browser)
import allure
from selenium.webdriver.common.by import By

from pages.BasePageHelper import BasePageHelper


class VKEcosystemLocators:
    LOGO_VK = (By.XPATH, '//a[@id="header-logo"]')

class VKEcosystemHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
            self.find_element(VKEcosystemLocators.LOGO_VK)

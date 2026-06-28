import allure

from pages.BasePageHelper import BasePageHelper
from selenium.webdriver.common.by import By

class LoginSocialLocators:
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[data-test-id="hero-register-btn"]')
    REGISTRATION_BY_PHONE_BUTTON = (By.CSS_SELECTOR, '[data-test-id="register-phone-toggle"]')

class LoginSocialHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик на кнопку регистрации")
    def click_registration_button(self):
        self.find_element(LoginSocialLocators.REGISTRATION_BUTTON).click()

    @allure.step("Клик на кнопку регистрации по номеру телефона")
    def click_register_by_phone_button(self):
        self.find_element(LoginSocialLocators.REGISTRATION_BY_PHONE_BUTTON).click()

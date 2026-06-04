import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-test-id="password-input"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test-id="enter-action"]')
    LOGIN_BY_QR_BUTTON = (By.XPATH, '//button[@label="Войти по QR-коду"]')
    SWITCH_LOGIN = (By.XPATH, '//*[@data-l="t,login_tab"]')
    SWITCH_QR = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//button[.//span[text()="Показать пароль"]]')
    RECOVER_ACCESS_BUTTON = (By.XPATH, '//button[@aria-label="Не получается войти?"]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[.//span[text()="Зарегистрироваться"]]')
    LOGIN_VIA_VK = [By.CSS_SELECTOR, '[data-l="t,vkc"]']
    LOGIN_VIA_MAIL = [By.CSS_SELECTOR, '[data-l="t,mailru"]']
    LOGIN_VIA_YANDEX = [By.CSS_SELECTOR, '[data-l="t,yandex"]']
    LOGIN_VIA_GOOGLE = [By.CSS_SELECTOR, '[data-l="t,google"]']
    LOGIN_VIA_APPLE = [By.CSS_SELECTOR, '[data-l="t,apple"]']
    LOGIN_ERROR_TEXT = [By.XPATH, '//*[text()="Введите логин"]']
    PASSWORD_ERROR_TEXT = [By.XPATH, '//*[text()="Введите пароль"]']


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BY_QR_BUTTON)
        self.find_element(LoginPageLocators.SWITCH_LOGIN)
        self.find_element(LoginPageLocators.SWITCH_QR)
        self.find_element(LoginPageLocators.SHOW_PASSWORD_BUTTON)
        self.find_element(LoginPageLocators.RECOVER_ACCESS_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_VIA_VK)
        self.find_element(LoginPageLocators.LOGIN_VIA_MAIL)
        self.find_element(LoginPageLocators.LOGIN_VIA_YANDEX)
        self.find_element(LoginPageLocators.LOGIN_VIA_GOOGLE)
        self.find_element(LoginPageLocators.LOGIN_VIA_APPLE)

    @allure.step("Клик на кнопку авторизации")
    def login_click(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Заполнение логина")
    def set_login(self, text):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text)

    @allure.step("Возврат текста ошибки о пустом логине")
    def get_error_login_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.LOGIN_ERROR_TEXT).text

    @allure.step("Возврат текста ошибки о пустом пароле")
    def get_error_password_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.PASSWORD_ERROR_TEXT).text
from pages import BasePage
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
    LOGIN_VIA_VK = ['title="Войти через VK ID"']
    LOGIN_VIA_MAIL = ['data-l="t,mailru"']
    LOGIN_VIA_YANDEX = ['data-l="t,yandex"']
    LOGIN_VIA_GOOGLE = ['data-l="t,google"']
    LOGIN_VIA_APPLE = ['data-l="t,apple"']

class LoginPageHelper(BasePage):
    pass
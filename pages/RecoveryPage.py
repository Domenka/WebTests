from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class RecoverPageLocators:
    SUPPORT_BUTTON = [By.XPATH, '//*[text()="Обратиться в службу поддержки"]']
    RECOVER_VIA_PHONE_BUTTON = [By.CSS_SELECTOR, '[data-l="t,phone"]']
    RECOVER_VIA_EMAIL_BUTTON = [By.CSS_SELECTOR, '[data-l="t,email"]']
    QR_CODE = [By.XPATH, '//*[@class="qr_code_image"]']

class RecoveryPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(RecoverPageLocators.SUPPORT_BUTTON)
        self.find_element(RecoverPageLocators.RECOVER_VIA_PHONE_BUTTON)
        self.find_element(RecoverPageLocators.RECOVER_VIA_EMAIL_BUTTON)
        self.find_element(RecoverPageLocators.QR_CODE)
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGO_BUTTON = (By.CSS_SELECTOR, '[id="nohook_logo_link"]')
    SERVICES_BUTTON = (By.XPATH, '//button[@aria-label="Сервисы VK"]')
    MORE_SERVICES_BUTTON = (By.CSS_SELECTOR, 'a[data-l="t,more"]')

class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def check_page(self):
        self.find_element(BasePageLocators.LOGO_BUTTON)
        self.find_element(BasePageLocators.SERVICES_BUTTON)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message="Element is not clickable."
        )

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_any_elements_located(locator),
            message="Elements are not visible."
        )

    @allure.step("Открытие страницы")
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "screenshot", allure.attachment_type.PNG)

    @allure.step("Нажатие на кнопку с различными сервисами")
    def click_vk_ecosystems(self):
        self.find_element(BasePageLocators.SERVICES_BUTTON).click()

    @allure.step("Нажатие на кнопку с другими сервисами")
    def click_more_services(self):
        self.find_element(BasePageLocators.MORE_SERVICES_BUTTON).click()

    def get_windows_id(self, index):
        return self.driver.window_handles[index]

    def switch_window(self, window_id):
        self.driver.switch_to.window(window_id)
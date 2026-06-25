import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

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
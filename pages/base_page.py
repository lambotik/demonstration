import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        with allure.step(f'Open page: {self.url}'):
            self.driver.get(self.url)

    def get_current_url(self):
        get_url = self.url
        return get_url

    def element_is_visible(self, locator, timeout=5):
        with allure.step(f'Check element is visible {locator}'):
            return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

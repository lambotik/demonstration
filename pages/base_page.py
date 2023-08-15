import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.time_out = 5

    def open(self):
        with allure.step(f'Open page: {self.url}'):
            self.driver.get(self.url)

    def get_current_url(self):
        get_url = self.url
        return get_url

    def element_is_visible(self, locator):
        with allure.step(f'Check element is visible {locator}'):
            return wait(self.driver, self.time_out).until(EC.visibility_of_element_located(locator))

    @allure.step('Check element is present')
    def element_is_present(self, locator):
        return wait(self.driver, self.time_out).until(EC.presence_of_element_located(locator))

    @allure.step('Attach screenshot')
    def attach_screenshot(self, element):
        """Create screenshot of current window and attach it in allure report
        Args:
         - file_name: str like 'Linkedin_button_not_found'
        """
        element_name = ''.join(element)
        allure.attach(self.driver.get_screenshot_as_png(), name=element_name, attachment_type=AttachmentType.PNG)

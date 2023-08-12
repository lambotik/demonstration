from pages.main_page import MainPage
import allure

@allure.suite('Test Main Page')
class TestMainPage:
    @allure.step('Test fill form')
    def test_fill_form(self, driver):
        test_elements = MainPage(driver, 'https://allcedo.ru/')
        test_elements.open()
        result = test_elements.ask_question()
        assert result == 'Спасибо!', 'Fail!!!'

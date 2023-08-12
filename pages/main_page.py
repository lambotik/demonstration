import time

import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()

    def ask_question(self):
        with allure.step('Click ASK_QUESTION'):
            self.element_is_present(self.locators.ASK_QUESTION).click()
        with allure.step('INPUT NAME: TEST'):
            self.element_is_present(self.locators.INPUT_NAME).send_keys('TEST')
        with allure.step('INPUT LAST NAME: TEST'):
            self.element_is_present(self.locators.INPUT_LAST_NAME).send_keys('TEST')
        with allure.step('INPUT COMPANY: TEST'):
            self.element_is_present(self.locators.INPUT_COMPANY).send_keys('TEST')
        with allure.step('INPUT SUBJECT: TEST'):
            self.element_is_present(self.locators.INPUT_SUBJECT).send_keys('TEST')
        with allure.step('INPUT EMAIL: test@it.ru'):
            self.element_is_present(self.locators.INPUT_EMAIL).send_keys('test@it.ru')
        with allure.step('INPUT MESSAGE: TEST'):
            self.element_is_present(self.locators.INPUT_MESSAGE).send_keys('TEST')
        with allure.step('Click: Я прочитал и принимаю'):
            self.element_is_present(self.locators.ACCEPT).click()
        with allure.step('Click: Отправить запрос'):
            self.element_is_present(self.locators.BUTTON_SEND_REQUEST).click()
        answer = self.element_is_present(self.locators.THANK)
        return answer.text

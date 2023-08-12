from selenium.webdriver.common.by import By


class MainPageLocators:
    ASK_QUESTION = (By.CSS_SELECTOR, "[alt= 'Задать вопрос']")
    INPUT_NAME = (By.CSS_SELECTOR, "[aria-label='Имя']")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "[aria-label='Фамилия']")
    INPUT_COMPANY = (By.CSS_SELECTOR, "[aria-label='Компания']")
    INPUT_SUBJECT = (By.CSS_SELECTOR, "[aria-label='Тема']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "[aria-label='Email']")
    INPUT_MESSAGE = (By.CSS_SELECTOR, "[aria-label='Сообщение']")
    ACCEPT = (By.CSS_SELECTOR, "div[class='q-item q-item-type row no-wrap accept-block q-pl-none q-mb-md'] "
                               "div[class='q-checkbox__bg absolute']")
    BUTTON_SEND_REQUEST = (By.XPATH, "//button[@class='q-btn q-btn-item non-selectable no-outline q-btn--unelevated "
                                     "q-btn--rectangle text-white q-btn--actionable "
                                     "q-focusable q-hoverable q-btn--dense bold']")
    THANK = (By.CSS_SELECTOR, "div[class='event-modal-message__title']")

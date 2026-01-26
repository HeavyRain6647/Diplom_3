# pages/main_page.py
from .base_page import BasePage
from locators import MainPageLocators  # <-- Простой импорт
from data import Urls

class MainPage(BasePage):
    def open(self):
        self.driver.get(Urls.BASE_URL)

    def click_login_to_account_button(self):
        self.find_element(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

    def click_personal_account_link(self):
        self.find_element(MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    
    def check_create_order_button_is_visible(self):
        return self.find_element(MainPageLocators.CREATE_ORDER_BUTTON).is_displayed()

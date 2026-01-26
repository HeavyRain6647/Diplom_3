# pages/login_page.py
from .base_page import BasePage
from locators import LoginPageLocators, RegisterPageLocators # <-- Простой импорт
from data import Urls

class LoginPage(BasePage):
    def open(self):
        self.driver.get(Urls.LOGIN_PAGE)

    def login_user(self, email, password):
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def register_user(self, name, email, password):
        self.find_element(RegisterPageLocators.NAME_INPUT).send_keys(name)
        self.find_element(RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        self.find_element(RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        self.find_element(RegisterPageLocators.REGISTER_BUTTON).click()

    def check_short_password_error_is_visible(self):
        return self.find_element(RegisterPageLocators.SHORT_PASSWORD_ERROR).is_displayed()

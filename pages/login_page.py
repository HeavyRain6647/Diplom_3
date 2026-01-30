# pages/login_page.py
import allure
from .base_page import BasePage
from locators import LoginPageLocators
from data import Urls

class LoginPage(BasePage):
    @allure.step("Ожидание загрузки страницы входа")
    def wait_for_load(self):
        # ИСПРАВЛЕНИЕ: Ждем появления кнопки "Войти", это самый надежный индикатор
        self.find_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Открытие страницы входа")
    def open(self):
        self.driver.get(Urls.LOGIN_PAGE)
        self.wait_for_load()

    @allure.step("Заполнение формы входа и клик по кнопке 'Войти'")
    def login_user(self, email, password):
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.wait_and_click(LoginPageLocators.LOGIN_BUTTON)

# pages/main_page.py
import allure
from .base_page import BasePage
from locators import MainPageLocators
from data import Urls

class MainPage(BasePage):
    @allure.step("Ожидание загрузки ингредиентов на главной странице")
    def wait_for_ingredients_load(self):
        self.find_element(MainPageLocators.INGREDIENTS_SECTION)

    @allure.step("Открытие главной страницы")
    def open(self):
        self.driver.get(Urls.BASE_URL)
        self.wait_for_ingredients_load()

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_to_account_button(self):
        self.wait_and_click(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)

    @allure.step("Клик по ссылке 'Личный Кабинет'")
    def click_personal_account_link(self):
        self.wait_and_click(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step("Создание заказа (клик по ингредиентам и кнопке 'Оформить заказ')")
    def create_order(self):
        self.wait_and_click(MainPageLocators.INGREDIENT_BUN)
        self.wait_and_click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_and_click(MainPageLocators.INGREDIENT_SAUCE)
        self.wait_and_click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_and_click(MainPageLocators.CREATE_ORDER_BUTTON)
        
        order_number = self.get_text(MainPageLocators.ORDER_NUMBER_IN_MODAL)
        self.wait_and_click(MainPageLocators.MODAL_CLOSE_BUTTON)
        return order_number

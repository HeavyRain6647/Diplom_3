# pages/main_page.py
import allure
from .base_page import BasePage
from locators import MainPageLocators
from data import Urls

class MainPage(BasePage):
    def wait_for_ingredients_load(self):
        self.find_element(MainPageLocators.INGREDIENTS_SECTION)

    def open(self):
        self.driver.get(Urls.BASE_URL)
        self.wait_for_ingredients_load()

    def click_login_to_account_button(self):
        self.wait_and_click(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)

    def click_personal_account_link(self):
        self.wait_and_click(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step("Создание заказа (надежная версия)")
    def create_order(self):
        # Шаг 1: Перетаскиваем булку.
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.CONSTRUCTOR_AREA)

        # Шаг 2: Ждем, пока кнопка "Оформить заказ" станет активной.
        self.wait_for_element_to_be_clickable(MainPageLocators.CREATE_ORDER_BUTTON)

        # Шаг 3: Перетаскиваем соус.
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.CONSTRUCTOR_AREA)
        
        # Шаг 4: Нажимаем на кнопку.
        self.wait_and_click(MainPageLocators.CREATE_ORDER_BUTTON)
        
        # Шаг 5: Ждем появления номера заказа.
        order_number = self.get_text(MainPageLocators.ORDER_NUMBER_IN_MODAL)
        
        # Шаг 6: Закрываем модальное окно.
        self.wait_and_click(MainPageLocators.MODAL_CLOSE_BUTTON)
        
        return order_number

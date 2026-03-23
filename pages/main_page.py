# pages/main_page.py
import allure
from .base_page import BasePage
from locators import MainPageLocators
from data import Urls

class MainPage(BasePage):
    @allure.step("Ожидание загрузки ингредиентов")
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

    @allure.step("Создание заказа (надежная версия)")
    def create_order(self):
        # Перетаскиваем булку и ЖДЕМ ее появления в конструкторе
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.CONSTRUCTOR_AREA)
        self.find_element(MainPageLocators.CONSTRUCTOR_BUN_ITEM)

        # Теперь, когда кнопка должна быть активна, нажимаем
        self.wait_and_click(MainPageLocators.CREATE_ORDER_BUTTON)
        
        # Получаем номер заказа и закрываем модальное окно
        order_number = self.get_text(MainPageLocators.ORDER_NUMBER_IN_MODAL)
        self.wait_and_click(MainPageLocators.MODAL_CLOSE_BUTTON)
        return order_number

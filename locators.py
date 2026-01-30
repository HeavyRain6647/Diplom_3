# locators.py
from selenium.webdriver.common.by import By

# --- Локаторы Главной страницы ---
class MainPageLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/..")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']/..")
    INGREDIENTS_SECTION = (By.XPATH, ".//h2[text()='Булки']")
    
    INGREDIENT_BUN = (By.XPATH, ".//p[text()='Краторная булка N-200i']/parent::a")
    INGREDIENT_SAUCE = (By.XPATH, ".//p[text()='Соус Spicy-X']/parent::a")
    
    CONSTRUCTOR_AREA = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    
    CONSTRUCTOR_BUN_ITEM = (By.XPATH, ".//span[text()='Краторная булка N-200i']")
    CONSTRUCTOR_SAUCE_ITEM = (By.XPATH, ".//span[text()='Соус Spicy-X']")

    ORDER_NUMBER_IN_MODAL = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")

# --- Локаторы Страницы входа ---
class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/../input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/../input")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")

# --- Локаторы Страницы профиля ---
class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль' and contains(@class, 'active')]")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

# --- Локаторы Страницы Ленты Заказов ---
class OrderFeedPageLocators:
    PAGE_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")
    STATS_BLOCK = (By.XPATH, ".//div[contains(@class, 'OrderFeed_stats')]")
    ALL_TIME_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня']/following-sibling::p")
    
    @staticmethod
    def get_order_in_progress_locator(order_number):
        number_without_zeros = str(int(order_number))
        return (By.XPATH, f".//p[text()='#{number_without_zeros}']")

# locators.py
from selenium.webdriver.common.by import By

# --- Локаторы Главной страницы ---
class MainPageLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/..")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    INGREDIENT_CARD = (By.XPATH, ".//ul[contains(@class, 'BurgerIngredients_ingredients__list')]/a[1]")
    INGREDIENT_DETAILS_MODAL = (By.XPATH, ".//div[contains(@class, 'Modal_modal__container')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']/..")
    ORDER_FEED_LINK = (By.XPATH, ".//p[text()='Лента Заказов']/..")

# --- Локаторы Страницы входа ---
class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/../input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/../input")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")

# --- Локаторы Страницы регистрации ---
class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/../input")
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/../input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/../input")
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    SHORT_PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")

# --- Локаторы Страницы профиля ---
class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль' and contains(@class, 'active')]")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

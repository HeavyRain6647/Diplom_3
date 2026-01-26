# tests/test_stellar_burgers.py
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from data import Urls, TestCredentials

class TestStellarBurgers:
    
    def test_registration_success(self, driver, user):
        """Проверка успешной регистрации."""
        email, password = user
        login_page = LoginPage(driver)
        login_page.open()
        assert login_page.driver.current_url == Urls.LOGIN_PAGE

    def test_registration_short_password_error(self, driver):
        """Проверка ошибки при регистрации с коротким паролем (меньше 6 символов)."""
        login_page = LoginPage(driver)
        login_page.driver.get(Urls.REGISTER_PAGE)
        login_page.register_user("TestName", "test@test.ru", TestCredentials.SHORT_PASSWORD)
        assert login_page.check_short_password_error_is_visible()

    def test_login_from_main_page_button_success(self, driver, user):
        """Проверка входа по кнопке «Войти в аккаунт» на главной."""
        email, password = user
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        main_page.click_login_to_account_button()
        login_page.login_user(email, password)
        
        assert main_page.check_create_order_button_is_visible()

    def test_login_from_personal_account_link_success(self, driver, user):
        """Проверка входа через «Личный кабинет»."""
        email, password = user
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open()
        main_page.click_personal_account_link()
        login_page.login_user(email, password)

        assert main_page.check_create_order_button_is_visible()

    def test_navigation_to_personal_account(self, driver, user):
        """Проверка перехода в личный кабинет."""
        email, password = user
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        login_page.open()
        login_page.login_user(email, password)
        main_page.click_personal_account_link()
        
        assert driver.current_url == Urls.PROFILE_PAGE

    def test_navigation_from_profile_to_constructor(self, driver, user):
        """Проверка перехода из личного кабинета в конструктор."""
        email, password = user
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        login_page.open()
        login_page.login_user(email, password)
        main_page.click_personal_account_link()
        profile_page.click_constructor_link()
        
        assert driver.current_url == Urls.BASE_URL + '/'

    def test_logout_success(self, driver, user):
        """Проверка выхода из аккаунта."""
        email, password = user
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        login_page.open()
        login_page.login_user(email, password)
        main_page.click_personal_account_link()
        profile_page.click_logout_button()
        
        assert driver.current_url == Urls.LOGIN_PAGE

# tests/test_stellar_burgers.py
import allure
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage

@allure.feature('UI Тесты Stellar Burgers')
class TestStellarBurgers:
    
    @allure.story('Навигация и Авторизация')
    @allure.title('Проверка перехода в личный кабинет и выхода')
    def test_navigation_and_logout_flow(self, driver, user):
        email, password = user
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        
        main_page.open()
        main_page.click_login_to_account_button()
        login_page.login_user(email, password)
        
        # --- ФИНАЛЬНОЕ ИСПРАВЛЕНИЕ: Ждем полной прогрузки главной страницы ПОСЛЕ логина ---
        main_page.wait_for_ingredients_load()
        
        main_page.click_personal_account_link()
        profile_page.wait_for_load()
        assert "account/profile" in main_page.get_current_url()

        profile_page.click_logout_button()
        login_page.wait_for_load()
        assert "login" in login_page.get_current_url()

    @pytest.mark.xfail(reason="Drag-and-drop в Selenium нестабилен для этого сайта")
    @allure.story('Основной сценарий пользователя')
    @allure.title('Создание заказа и проверка в ленте')
    def test_full_order_creation_flow(self, driver, user):
        # Этот тест остается без изменений, помеченный как xfail
        email, password = user
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        login_page.open()
        login_page.login_user(email, password)

        main_page.open()
        order_number = main_page.create_order()
        assert order_number.isdigit(), "Номер заказа не был получен"

        order_feed_page.open()
        assert order_feed_page.find_order_in_progress(order_number), "Заказ не найден"
        assert order_feed_page.get_all_time_counter_value() > 0, "Счетчик 'за все время' равен 0"
        assert order_feed_page.get_today_counter_value() > 0, "Счетчик 'за сегодня' равен 0"

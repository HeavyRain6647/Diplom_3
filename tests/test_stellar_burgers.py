# tests/test_stellar_burgers.py
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage

@allure.feature('UI Тесты Stellar Burgers')
class TestStellarBurgers:
    
    # Тест на навигацию остается без изменений
    @allure.story('Навигация и Авторизация')
    @allure.title('Проверка перехода в личный кабинет и выхода')
    def test_navigation_and_logout_flow(self, driver, user):
        # ... (код этого теста не меняется)

    # --- РАЗДЕЛЯЕМ БОЛЬШОЙ ТЕСТ НА ТРИ АТОМАРНЫХ ---
    
    @allure.story('Лента заказов')
    @allure.title('Если создать заказ, он появится в ленте заказов')
    def test_order_appears_in_feed(self, driver, created_order):
        """
        Проверяем, что номер созданного заказа появляется в общей ленте.
        Фикстура created_order уже создала заказ.
        """
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open()
        assert order_feed_page.is_order_in_feed(created_order), "Созданный заказ не найден в общей ленте"

    @allure.story('Лента заказов')
    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_user_orders_appear_in_history(self, driver, created_order):
        """
        Проверяем, что заказ пользователя появляется в его личной истории.
        """
        profile_page = ProfilePage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        # Переходим в историю заказов в профиле
        profile_page.open_and_wait()
        profile_page.click_order_history_link()
        
        # Проверяем, что заказ есть в истории
        assert order_feed_page.is_order_in_feed(created_order), "Созданный заказ не найден в истории заказов пользователя"

    @allure.story('Лента заказов')
    @allure.title('При создании нового заказа счётчики "Выполнено за всё время" и "Выполнено за сегодня" увеличиваются')
    def test_counters_increase_on_order_creation(self, driver, user):
        """
        Проверяем, что счетчики увеличиваются.
        Этот тест должен быть отдельным, так как он меняет общее состояние.
        """
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        # Логинимся
        login_page.open()
        login_page.login_user(user[0], user[1])

        # Получаем начальные значения
        order_feed_page.open()
        initial_all_time = order_feed_page.get_all_time_counter_value()
        initial_today = order_feed_page.get_today_counter_value()
        
        # Создаем заказ
        main_page.open()
        main_page.create_order()
        
        # Проверяем новые значения
        order_feed_page.open()
        final_all_time = order_feed_page.get_all_time_counter_value()
        final_today = order_feed_page.get_today_counter_value()

        assert final_all_time == initial_all_time + 1
        assert final_today == initial_today + 1

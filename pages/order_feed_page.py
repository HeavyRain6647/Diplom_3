# pages/order_feed_page.py
import allure
from .base_page import BasePage
from locators import OrderFeedPageLocators
from data import Urls

class OrderFeedPage(BasePage):
    @allure.step("Ожидание загрузки блока статистики")
    def wait_for_load(self):
        # ИСПРАВЛЕНИЕ ЗДЕСЬ: Ждем появления всего блока со статистикой
        self.find_element(OrderFeedPageLocators.STATS_BLOCK)

    @allure.step("Открытие страницы 'Лента Заказов' и ожидание загрузки")
    def open(self):
        self.driver.get(Urls.FEED_PAGE)
        self.wait_for_load()
    
    def get_all_time_counter_value(self):
        return int(self.get_text(OrderFeedPageLocators.ALL_TIME_COUNTER).replace(',', ''))

    def get_today_counter_value(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_COUNTER).replace(',', ''))

    def find_order_in_progress(self, order_number):
        order_locator = OrderFeedPageLocators.get_order_in_progress_locator(order_number)
        return self.find_element(order_locator, time=20).is_displayed()

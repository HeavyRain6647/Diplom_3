import allure
from selenium.webdriver import ActionChains
from locators.locators import MainPageLocators, FeedPageLocators
from pages.base_page import BasePage

class TestMainFunctionality:

    @allure.title("Проверка открытия модального окна с деталями ингредиента")
    def test_open_ingredient_details(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        page = BasePage(driver)
        page.click(MainPageLocators.INGREDIENT_CARD)
        modal = page.find_element(MainPageLocators.MODAL_WINDOW)
        assert modal.is_displayed()

    @allure.title("Проверка увеличения счетчика при добавлении в корзину")
    def test_ingredient_counter_increase(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        page = BasePage(driver)
        
        ingredient = page.find_element(MainPageLocators.BUN_INGREDIENT)
        basket = page.find_element(MainPageLocators.BASKET_AREA)
        
        actions = ActionChains(driver)
        actions.drag_and_drop(ingredient, basket).perform()
        
        counter_value = page.get_text(MainPageLocators.COUNTER)
        assert int(counter_value) > 0

class TestOrderFeed:
    @allure.title("Проверка перехода в Ленту заказов")
    def test_go_to_feed(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        page = BasePage(driver)
        page.click(MainPageLocators.ORDER_FEED_LINK)
        assert "/feed" in driver.current_url
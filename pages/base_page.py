# pages/base_page.py
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору {locator}"
        )

    @allure.step("Ожидание, пока элемент станет кликабельным")
    def wait_for_element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Клик по элементу (с ожиданием)")
    def wait_and_click(self, locator, time=10):
        element = self.wait_for_element_to_be_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Перетаскивание элемента с помощью JavaScript")
    def drag_and_drop_element(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        
        # --- ИСПОЛЬЗУЕМ ВАШ JAVASCRIPT ДЛЯ DRAG-AND-DROP ---
        script = """
            var source = arguments[0];
            var target = arguments[1];
            var evt = new DragEvent("dragstart", { bubbles: true, cancelable: true });
            source.dispatchEvent(evt);
            var dropEvt = new DragEvent("drop", { bubbles: true, cancelable: true });
            target.dispatchEvent(dropEvt);
            var dragEndEvt = new DragEvent("dragend", { bubbles: true, cancelable: true });
            source.dispatchEvent(dragEndEvt);
        """
        # Я немного упростил скрипт, оставив только ключевые события, которые обычно нужны React
        self.driver.execute_script(script, source, target)

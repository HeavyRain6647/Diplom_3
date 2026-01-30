# pages/profile_page.py
import allure
from .base_page import BasePage
from locators import ProfilePageLocators, MainPageLocators

class ProfilePage(BasePage):
    @allure.step("Ожидание загрузки страницы Профиля")
    def wait_for_load(self):
        # ИСПРАВЛЕНИЕ: Ждем появления уникального элемента страницы
        self.find_element(ProfilePageLocators.PROFILE_LINK)

    def click_logout_button(self):
        self.wait_and_click(ProfilePageLocators.LOGOUT_BUTTON)

    def click_constructor_link(self):
        self.wait_and_click(MainPageLocators.CONSTRUCTOR_LINK)

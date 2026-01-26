# pages/profile_page.py
from .base_page import BasePage
from locators import ProfilePageLocators, MainPageLocators # <-- Простой импорт

class ProfilePage(BasePage):
    def check_profile_link_is_active(self):
        return self.find_element(ProfilePageLocators.PROFILE_LINK).is_displayed()

    def click_logout_button(self):
        self.find_element(ProfilePageLocators.LOGOUT_BUTTON).click()

    def click_constructor_link(self):
        self.find_element(MainPageLocators.CONSTRUCTOR_LINK).click()

# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage # Импортируем MainPage
import requests
import random
import string
from data import Urls

def pytest_addoption(parser):
    # ... (код для выбора браузера остается без изменений)
    parser.addoption(
        '--browser_name', action='store', default='chrome',
        help="Выберите браузер: chrome или firefox"
    )

# ... (фикстура driver и user остаются без изменений)
@pytest.fixture(scope='function')
def driver(request):
    # ... (код фикстуры driver)
    browser_name = request.config.getoption("browser_name")
    # ...
    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    # ...
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def user():
    # ... (код фикстуры user)
    # ...
    yield email, password
    # ...

# --- НОВАЯ ФИКСТУРА ДЛЯ СОЗДАНИЯ ЗАКАЗА ---
@pytest.fixture(scope="function")
def created_order(driver, user):
    """
    Логинится под пользователем, создает один заказ и возвращает его номер.
    """
    # Эта фикстура использует другие фикстуры: driver и user
    from pages.login_page import LoginPage # Локальный импорт, чтобы не было циклических зависимостей
    
    email, password = user
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    
    login_page.open()
    login_page.login_user(email, password)
    main_page.open()
    order_number = main_page.create_order()
    
    return order_number

# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage
import requests
import random
import string
from data import Urls

def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default='chrome',
        help="Выберите браузер: chrome или firefox"
    )

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

@pytest.fixture(scope='function')
def driver(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def user():
    #
    # --- ВОССТАНАВЛИВАЕМ ПОЛНЫЙ КОД ФИКСТУРЫ USER ---
    #
    email = f"{generate_random_string()}@ya.ru"
    password = generate_random_string(8)
    name = generate_random_string()
    
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(Urls.API_REGISTER, json=payload)
    token = response.json().get("accessToken")
    
    yield email, password
    
    if token:
        requests.delete(Urls.API_USER, headers={"Authorization": token})

@pytest.fixture(scope="function")
def created_order(driver, user):
    from pages.login_page import LoginPage
    
    email, password = user
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    
    login_page.open()
    login_page.login_user(email, password)
    main_page.open()
    order_number = main_page.create_order()
    
    return order_number

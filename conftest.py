# conftest.py
import pytest
from selenium import webdriver
# Импортируем Service и Manager для обоих браузеров
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
# Остальные импорты
import requests
import random
import string
from data import Urls

def pytest_addoption(parser):
    # Добавляем опцию --browser_name в командную строку
    # По умолчанию будет запускаться 'chrome'
    parser.addoption(
        '--browser_name', action='store', default='chrome',
        help="Выберите браузер: chrome или firefox"
    )

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

@pytest.fixture(scope='function')
def driver(request):
    # Получаем значение --browser_name из командной строки
    browser_name = request.config.getoption("browser_name")
    
    driver = None
    if browser_name.lower() == "chrome":
        # --- Настройки для Chrome ---
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif browser_name.lower() == "firefox":
        # --- Настройки для Firefox ---
        options = webdriver.FirefoxOptions()
        # options.add_argument("-headless") # если нужно запустить в фоне
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    else:
        raise pytest.UsageError("--browser_name должен быть 'chrome' или 'firefox'")

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def user():
    """Создает пользователя через API и удаляет его после теста."""
    email = f"{generate_random_string()}@ya.ru"
    password = generate_random_string(8)
    name = generate_random_string()
    
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(Urls.API_REGISTER, json=payload)
    token = response.json().get("accessToken")
    
    yield email, password
    
    if token:
        requests.delete(Urls.API_USER, headers={"Authorization": token})

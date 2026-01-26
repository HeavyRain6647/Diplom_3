# conftest.py
import pytest
from selenium import webdriver
import requests
import random
import string
from data import Urls

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
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

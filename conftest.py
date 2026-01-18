import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    driver.maximize_window()
    yield driver
    driver.quit()
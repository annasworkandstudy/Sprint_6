import pytest
from selenium import webdriver
from helpers import OrderDataHelper
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    driver=webdriver.Firefox()
    url = "https://qa-scooter.praktikum-services.ru/" 
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
def data_for_order():
    return OrderDataHelper.generate_order_data()

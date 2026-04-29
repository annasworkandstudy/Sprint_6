import pytest
from selenium import webdriver
import random
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
    names = ["Иван", "Ян", "Константин", "Ли", "Александр", "Анна", "Дмитрий", "Мария"]
    name = f'Екатерина{random.choice(names)}'
    surnames = ["Иванов", "Петрова", "Сидоров", "Кузнецова", "Смирнов", "Попова", "Васильев", "Соколова"]
    surname = f'Иванова{random.choice(surnames)}'
    adress = f'Москва, ул.Софийская Набережная, д.{random.randint(100, 200)}'
    telephone = f'+7{random.randint(100000000, 999999999)}'
    date = f'{random.randint(1, 30)}.{random.randint(5,12)}.2026'
    comment = f'Комментарий'
    return name, surname, adress, telephone, date, comment

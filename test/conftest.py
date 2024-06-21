import random
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX
from constants import Constants
from locators import Locators


#Открытие сайта
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser

    browser.quit()


#Вход на сайт
@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
        By.CLASS_NAME, "Auth_login__3hAey"
    )))
    driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.AUTH_BUTTON).click()
    return driver


#Генерация случайного имени и email
@pytest.fixture
def fake_email(driver):
    faker = Faker()
    return {
        'name': faker.name(),
        'email': faker.email()
    }


#Генерация случайного пароля
@pytest.fixture
def fake_password(driver):
    return {
        'true_pass': random.randint(100000, 999999),
        'false_pass': random.randint(10, 99999)
    }
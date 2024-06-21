from selenium.webdriver.common.by import By


class Locators:
    NAME = (By.XPATH, "//label[contains(text(), 'Имя')]/../input") #Поле Имя
    EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/../input") #Поле Email
    PASSWORD = (By.CSS_SELECTOR, "input[name='Пароль']") #Поле Пароль
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']") #Кнопка Войти в аккаунт
    AUTH_BUTTON = (By.XPATH, "//button[text()='Войти']") #Кнопка Войти
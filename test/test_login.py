from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EX
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators


class TestLogin:
    #Тест входа через кнопку "Войти в аккаунт"
    def test_login_via_main_page_button(self, login):
        driver = login
        log = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//button[contains(text(),'Оформить заказ')]"
        )))
        assert log.is_displayed()

    #Тест входа через "Личный кабинет"
    def test_login_via_personal_account_button(self, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        log = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//button[contains(text(),'Оформить заказ')]"
        )))
        assert log.is_displayed()

    #Тест входа через форму регистрации
    def test_login_via_registration_form_button(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//a[contains(text(),'Зарегистрироваться')]"
        ))).click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//a[contains(text(),'Войти')]"
        ))).click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//label[contains(text(), 'Email')]/../input"
        )))
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        log = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//button[contains(text(),'Оформить заказ')]"
        )))
        assert log.is_displayed()

    #Тест входа через форму восстановления пароля
    def test_login_via_password_recovery_form_button(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(By.XPATH, "//button[contains(text(),'Восстановить')]").click()
        message = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//label[contains(text(),'Введите код из письма')]"
        )))
        assert message.is_displayed()

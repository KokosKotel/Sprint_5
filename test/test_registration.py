from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EX
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestRegistration:
    #Тест успешной регистрации
    def test_successful_registration(self, driver, fake_email, fake_password):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.CLASS_NAME, "Auth_login__3hAey"
        )))
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.CLASS_NAME, "Auth_login__3hAey"
        )))
        driver.find_element(*Locators.NAME).send_keys(fake_email['name'])
        driver.find_element(*Locators.EMAIL).send_keys(fake_email['email'])
        driver.find_element(*Locators.PASSWORD).send_keys(fake_password['true_pass'])
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 3).until(EX.url_contains("login"))
        assert "login" in driver.current_url

    #Тест появления ошибки при некорректном пароле
    def test_incorrect_password_error(self, driver, fake_email, fake_password):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.CLASS_NAME, "Auth_login__3hAey"
        )))
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.CLASS_NAME, "Auth_login__3hAey"
        )))
        driver.find_element(*Locators.NAME).send_keys(fake_email['name'])
        driver.find_element(*Locators.EMAIL).send_keys(fake_email['email'])
        driver.find_element(*Locators.PASSWORD).send_keys(fake_password['false_pass'])
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        error_message = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//p[contains(text(),'Некорректный пароль')]"
        )))
        assert error_message.is_displayed()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX
from locators import Locators


class TestLogout:
    #Тест выхода из аккаунта
    def test_logout_from_account(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.ACCOUNT_BUTTON
        )))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.LOGOUT_BUTTON
        )))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        logout = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.ENTER_TEXT
        )))
        assert logout.is_displayed()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX


class TestLogout:
    #Тест выхода из аккаунта
    def test_logout_from_account(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
        ))).click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//button[contains(text(),'Выход')]"
        ))).click()
        logout = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//h2[contains(text(),'Вход')]"
        )))
        assert logout.is_displayed()

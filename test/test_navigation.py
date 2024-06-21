from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX


class TestNavigation:
    #Тест перехода в "Личный кабинет"
    def test_navigation_to_personal_account(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
        ))).click()
        history = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//a[contains(text(),'История заказов')]"
        )))
        assert history.is_displayed()

    #Тест перехода из "Личного кабинета" в "Конструктор"
    def test_navigation_from_personal_account_to_constructor(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
        ))).click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//p[contains(text(),'Конструктор')]"
        ))).click()
        message = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//h1[contains(text(),'Соберите бургер')]"
        )))
        assert message.is_displayed()

    #Тест перехода из "Личного кабинета" по клику на логотип
    def test_navigation_from_personal_account_by_click_logo(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
        ))).click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.CLASS_NAME, "AppHeader_header__logo__2D0X2"
        ))).click()
        message = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//h1[contains(text(),'Соберите бургер')]"
        )))
        assert message.is_displayed()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX
from locators import Locators


class TestNavigation:
    #Тест перехода в "Личный кабинет"
    def test_navigation_to_personal_account(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.ACCOUNT_BUTTON
        )))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        history = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.HISTORY_LINK
        )))
        assert history.is_displayed()

    #Тест перехода из "Личного кабинета" в "Конструктор"
    def test_navigation_from_personal_account_to_constructor(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.ACCOUNT_BUTTON
        )))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.CONSTRUCTOR_BUTTON
        )))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        message = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.MAIN_TEXT
        )))
        assert message.is_displayed()

    #Тест перехода из "Личного кабинета" по клику на логотип
    def test_navigation_from_personal_account_by_click_logo(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.ACCOUNT_BUTTON
        )))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.LOGO_LINK
        )))
        driver.find_element(*Locators.LOGO_LINK).click()
        message = WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.MAIN_TEXT
        )))
        assert message.is_displayed()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX
from locators import Locators


class TestNavigationConstructs:
    #Тест перехода в раздел "Булки"
    def test_navigation_to_buns_section(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.ORDER_BUTTON
        )))
        driver.find_element(*Locators.SAUCES_TEXT).click()
        driver.find_element(*Locators.BUNS_TEXT).click()
        buns_tab = driver.find_element(*Locators.SELECTED_SECTION)
        assert buns_tab.is_displayed()

    #Тест перехода в раздел "Соусы"
    def test_navigation_to_sauces_section(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.ORDER_BUTTON
        )))
        driver.find_element(*Locators.SAUCES_TEXT).click()
        sauces_tab = driver.find_element(*Locators.SELECTED_SECTION)
        assert sauces_tab.is_displayed()

    #Тест перехода в раздел "Начинка"
    def test_navigation_to_fillings_section(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            Locators.ORDER_BUTTON
        )))
        driver.find_element(*Locators.FILLING_TEXT).click()
        fillings_tab = driver.find_element(*Locators.SELECTED_SECTION)
        assert fillings_tab.is_displayed()

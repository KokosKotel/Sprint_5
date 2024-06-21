from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX


class TestNavigationConstructs:
    #Тест перехода в раздел "Булки"
    def test_navigation_to_buns_section(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//button[contains(text(),'Оформить заказ')]"
        )))
        name_buns = driver.find_element(By.XPATH, "//p[contains(text(),'Краторная булка N-200i')]")
        assert name_buns.is_displayed()

    #Тест перехода в раздел "Соусы"
    def test_navigation_to_sauces_section(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//span[contains(text(),'Соусы')]"
        ))).click()
        name_sauces = driver.find_element(By.XPATH, "//p[contains(text(),'Соус с шипами Антарианского плоскоходца')]")
        assert name_sauces.is_displayed()

    #Тест перехода в раздел "Начинка"
    def test_navigation_to_fillings_section(self, login):
        driver = login
        WebDriverWait(driver, 3).until(EX.visibility_of_element_located((
            By.XPATH, "//span[contains(text(),'Начинки')]"
        ))).click()
        name_fillings = driver.find_element(By.XPATH, "//p[contains(text(),'Сыр с астероидной плесенью')]")
        driver.execute_script("arguments[0].scrollIntoView();", name_fillings)
        assert name_fillings.is_displayed()

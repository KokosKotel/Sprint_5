from selenium.webdriver.common.by import By


class Locators:
    #Поля Имя, Email и Пароль
    NAME = (By.XPATH, "//label[contains(text(), 'Имя')]/../input")
    EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/../input")
    PASSWORD = (By.CSS_SELECTOR, "input[name='Пароль']")

    #Кнопки Войти в аккаунт, Войти, Выход, Личный кабинет,
    #Оформить заказ, Зарегистрироваться, Восстановить, Конструктор
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    AUTH_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    #Ссылки Логотип, Войти, Зарегистрироваться, Восстановить пароль, История заказов
    LOGO_LINK = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    AUTH_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    RECOVERY_LINK = (By.LINK_TEXT, "Восстановить пароль")
    HISTORY_LINK = (By.XPATH, "//a[contains(text(),'История заказов')]")


    #Текст Вход, Соберите бургер, Булки, Соусы, Начинки,
    #Поле для проверки формы восстановления пароля
    ENTER_TEXT = (By.XPATH, "//h2[contains(text(),'Вход')]")
    MAIN_TEXT = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
    BUNS_TEXT = (By.XPATH, "//span[contains(text(),'Булки')]")
    SAUCES_TEXT = (By.XPATH, "//span[contains(text(),'Соусы')]")
    FILLING_TEXT = (By.XPATH, "//span[contains(text(),'Начинки')]")
    RECOVERY_MESS = (By.XPATH, "//label[contains(text(),'Введите код из письма')]")

    #Локаторы для проверки выбраного раздела конструктора и для ошибки неккоректного пароля
    SELECTED_SECTION = (By.XPATH, "//div[contains(@class,'tab_tab_type_current__2BEPc')]")
    INCORRECT_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")

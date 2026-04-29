from selenium.webdriver.common.by import By

class LogoLocators:
    #Логотипы в верхней части страницы
    LOGO_YANDEX = (By.XPATH, ".//img[@alt='Yandex']")
    LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']")
    HEADER_ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать']")
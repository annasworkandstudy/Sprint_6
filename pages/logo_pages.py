import allure
from locators.logo_locators import LogoLocators
from selenium.webdriver.support import expected_conditions as EC

class LogoPages:
    def __init__(self, driver, wait):
        self.driver=driver
        self.wait = wait

    @allure.description('Проверяем, что главная страница открыта')
    def check_open_page(self):
        return self.driver.current_url
    
    @allure.step('Переходим на страницу заказа')
    def push_order_button(self):
        self.wait.until(EC.element_to_be_clickable(LogoLocators.HEADER_ORDER_BUTTON)).click()
    
    @allure.step('Кликаем на логотип Самокат')
    def click_logo_scooter(self):
        self.driver.find_element(*LogoLocators.LOGO_SCOOTER).click()

    @allure.step('Кликаем на логотип Яндекс')
    def click_logo_yandex(self):
        self.driver.find_element(*LogoLocators.LOGO_YANDEX).click()
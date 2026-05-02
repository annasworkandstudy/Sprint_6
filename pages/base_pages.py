import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.important_questions_locators import QuestionPageLocators

class BasePage:
    @allure.step('Проверяем текущий URL')
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Поиск элемента по локатору: {locator}')
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Клик по элементу: {locator}')
    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Очистка поля и ввод текста "{text}" в элемент {locator}')
    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Прокрутка страницы до элемента: {locator}')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Ожидание видимости элемента: {locator}')
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Переключение на новую вкладку')
    def switch_to_next_tab(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    @allure.step('Ожидание появления части "{url_part}" в URL')
    def wait_url_contains(self, url_part):
        return self.wait.until(EC.url_contains(url_part))
    
    @allure.step('Принять cookie')
    def accept_cookies(self):
        if self.driver.find_element(*QuestionPageLocators.COOKIE_BUTTON):
            self.driver.find_element(*QuestionPageLocators.COOKIE_BUTTON).click()


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.important_questions_locators import QuestionPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def switch_to_next_tab(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    def wait_url_contains(self, url_part):
        return self.wait.until(EC.url_contains(url_part))
    
    def accept_cookies(self):
        if self.driver.find_element(*QuestionPageLocators.COOKIE_BUTTON):
            self.driver.find_element(*QuestionPageLocators.COOKIE_BUTTON).click()


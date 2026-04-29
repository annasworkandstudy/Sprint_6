import allure
from locators.important_questions_locators import QuestionPageLocators

class QuestionPage:
    def __init__(self, driver):
        self.driver=driver

    @allure.description('Проверяем, что главная страница открыта')
    def check_open_page(self):
        return self.driver.current_url
    
    @allure.step('Скролим до раздела Вопросы о важном')
    def scroll_to_important(self):
        element=self.driver.find_element(*QuestionPageLocators.IMPORTANT_BLOCK)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ищем вопрос {question_locator} и раскрываем')
    def find_question(self, question_locator):
        self.driver.find_element(*question_locator).click()

    @allure.step('Получаем текст ответа {answer_locator}')
    def get_text(self, answer_locator):
        return self.driver.find_element(*answer_locator).text
    
    @allure.step('Принимаем куки')
    def accept_cookies(self):
        if self.driver.find_element(*QuestionPageLocators.COOKIE_BUTTON):
            self.driver.find_element(*QuestionPageLocators.COOKIE_BUTTON).click()
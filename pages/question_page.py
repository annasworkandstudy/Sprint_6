import allure
from pages.base_pages import BasePage
from locators.important_questions_locators import QuestionPageLocators

class QuestionPage(BasePage):

    @allure.step('Проверяем, что главная страница открыта')
    def check_open_page(self):
        return self.get_current_url()
    
    @allure.step('Скролим до раздела Вопросы о важном')
    def scroll_to_important(self):
        self.scroll_to_element(QuestionPageLocators.IMPORTANT_BLOCK)

    @allure.step('Кликаем на вопрос')
    def find_question(self, question_locator):
        self.click_element(question_locator)

    @allure.step('Получаем текст ответа')
    def get_text(self, answer_locator):
        element = self.wait_for_visibility(answer_locator)
        return element.text

    @allure.step('Получаем ответ на выбранный вопрос')
    def get_faq_answer(self, question_locator, answer_locator):
        self.scroll_to_important()
        self.click_question(question_locator)
        return self.get_answer_text(answer_locator)
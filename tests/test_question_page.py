import allure
from pages.question_page import QuestionPage
from locators.important_questions_locators import QuestionPageLocators
import pytest

class TestQuestionPage:
    @allure.title('Проверка вопросов и ответов на соответствие в разделе Вопросы о важном')
    @pytest.mark.parametrize("q_locator, a_locator, expected_text", [
        (QuestionPageLocators.QUESTION_0,QuestionPageLocators.ANSWER_0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (QuestionPageLocators.QUESTION_1,QuestionPageLocators.ANSWER_1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (QuestionPageLocators.QUESTION_2,QuestionPageLocators.ANSWER_2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (QuestionPageLocators.QUESTION_3,QuestionPageLocators.ANSWER_3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (QuestionPageLocators.QUESTION_4,QuestionPageLocators.ANSWER_4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (QuestionPageLocators.QUESTION_5,QuestionPageLocators.ANSWER_5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (QuestionPageLocators.QUESTION_6,QuestionPageLocators.ANSWER_6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (QuestionPageLocators.QUESTION_7,QuestionPageLocators.ANSWER_7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])

    def test_question_page(self, driver, q_locator, a_locator, expected_text ):
        page=QuestionPage(driver)
        page.accept_cookies()
        page.scroll_to_important()
        page.find_question(q_locator)
        assert page.get_text(a_locator) == expected_text

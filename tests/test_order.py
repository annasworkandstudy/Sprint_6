import allure
from pages.order_page import OrderPage
from pages.question_page import QuestionPage
from locators.order_locators import OrderButtonLocators
import pytest

class TestOrderPage:
    @allure.title('Тест с параметризацией по кнопке Заказать')
    @allure.description('Появления всплывающего окна с сообщением об успешном создании заказа')
    @pytest.mark.parametrize("BUTTON_ORDER, COLOUR_LOCATOR", [
        (OrderButtonLocators.HEADER_ORDER_BUTTON, OrderButtonLocators.CHOOSE_COLOUR_BLACK),
        (OrderButtonLocators.HEADER_ORDER_BUTTON, OrderButtonLocators.CHOOSE_GREY_COLOUR),
        (OrderButtonLocators.FOOTER_ORDER_BUTTON, OrderButtonLocators.CHOOSE_COLOUR_BLACK),
        (OrderButtonLocators.FOOTER_ORDER_BUTTON, OrderButtonLocators.CHOOSE_GREY_COLOUR)
        ])
    def test_order_scooter(self, driver, data_for_order, BUTTON_ORDER, COLOUR_LOCATOR):
        page = OrderPage(driver)
        question_page = QuestionPage(driver)
        question_page.accept_cookies()
        page.push_order_button(BUTTON_ORDER)
        result_text = page.set_order_form(data_for_order, COLOUR_LOCATOR)
        assert "Заказ оформлен" in result_text

        
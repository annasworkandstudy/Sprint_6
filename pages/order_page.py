import allure
from selenium.webdriver.common.keys import Keys
from pages.base_pages import BasePage
from locators.order_locators import OrderButtonLocators

class OrderPage(BasePage):

    @allure.step('Проверяем текущий URL')
    def check_open_page(self):
        return self.get_current_url()
    
    @allure.step('Клик по кнопке Заказать')
    def push_order_button(self, locator_order_button):
        if locator_order_button == OrderButtonLocators.FOOTER_ORDER_BUTTON:
            self.scroll_to_element(locator_order_button)
        self.click_element(locator_order_button)

    @allure.step('Заполнение поля Имя')
    def set_input_name(self, name):
        self.set_text(OrderButtonLocators.INPUT_NAME, name)
    
    @allure.step('Заполнение поля Фамилия')
    def set_input_surname(self, surname):
        self.set_text(OrderButtonLocators.INPUT_SURNAME, surname)

    @allure.step('Заполнение поля Адрес')
    def set_input_adress(self, address):
        self.set_text(OrderButtonLocators.INPUT_ADRESS, address)

    @allure.step('Заполнение поля Станция метро')
    def set_input_undeground(self):
        element = self.find_element(OrderButtonLocators.INPUT_UNDEGROUND)
        element.send_keys('Черкизовская')
        element.send_keys(Keys.DOWN, Keys.ENTER)

    @allure.step('Заполнение поля Телефон')
    def set_input_telephone(self, phone):
        self.set_text(OrderButtonLocators.INPUT_PHONE, phone)

    @allure.step('Переход на форму Про аренду')
    def click_next(self):
        self.click_element(OrderButtonLocators.NEXT_BUTTON)

    @allure.step('Заполнение поля Когда привезти самокат')
    def set_input_bring(self, date):
        element = self.find_element(OrderButtonLocators.INPUT_BRING)
        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    @allure.step('Заполнение поля Срок аренды')
    def set_input_rent(self):
        self.click_element(OrderButtonLocators.INPUT_RENT)
        self.click_element(OrderButtonLocators.CHOOSE_RENTAL_PERIOD)

    @allure.step('Выбор цвета самоката')
    def choose_colour(self, colour_scooter):
        self.click_element(colour_scooter)

    @allure.step('Заполнение комментария')
    def set_input_comment(self, comment):
        self.set_text(OrderButtonLocators.COMMENT, comment)
    
    @allure.step('Подтверждение заказа')
    def confirm(self):
        self.click_element(OrderButtonLocators.BUTTON_ORDER_IN_FORM)

    @allure.step('Ожидаем появления окна с сообщением об успехе')
    def wait_message_success_order(self):
        self.click_element(OrderButtonLocators.CONFIRMATION_ORDER)
        return self.wait_for_visibility(OrderButtonLocators.SUCCESSFUL_ORDER).text

    @allure.step('Кликаем на логотип Самокат')
    def click_logo_scooter(self):
        self.click_element(OrderButtonLocators.LOGO_SCOOTER)

    @allure.step('Кликаем на логотип Яндекс')
    def click_logo_yandex(self):
        self.click_element(OrderButtonLocators.LOGO_YANDEX)

    @allure.step('Заполняем поля формы заказа')
    def set_order_form(self, data, colour_scooter):
        name, surname, address, telephone, date, comment = data
        self.set_input_name(name)
        self.set_input_surname(surname)
        self.set_input_adress(address)
        self.set_input_undeground()
        self.set_input_telephone(telephone)
        self.click_next()
        self.wait_for_visibility(OrderButtonLocators.INPUT_BRING)
        self.set_input_bring(date)
        self.set_input_rent()
        self.choose_colour(colour_scooter)
        self.set_input_comment(comment)
        self.confirm()
        return self.wait_message_success_order()
    

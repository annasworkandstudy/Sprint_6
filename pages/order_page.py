import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderButtonLocators
from selenium.webdriver.common.keys import Keys

class OrderPage:
    def __init__(self, driver, wait):
        self.driver=driver
        self.wait=wait
    
    @allure.description('Проверяем, что главная страница открыта')
    def check_open_page(self):
        return self.driver.current_url
    
    @allure.step('Клик по кнопке Заказать')
    def push_order_button(self, locator_order_button):
        if locator_order_button == OrderButtonLocators.FOOTER_ORDER_BUTTON:
            element = self.wait.until(EC.presence_of_element_located(locator_order_button))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable(locator_order_button)).click()

    @allure.step('Заполнение поля Имя')
    def set_input_name(self, name):
        self.driver.find_element(*OrderButtonLocators.INPUT_NAME).send_keys(name)
    
    @allure.step('Заполнение поля Фамилия')
    def set_input_surname(self, surname):
        self.driver.find_element(*OrderButtonLocators.INPUT_SURNAME).send_keys(surname)

    @allure.step('Заполнение поля Адрес')
    def set_input_adress(self, address):
        self.driver.find_element(*OrderButtonLocators.INPUT_ADRESS).send_keys(address)

    @allure.step('Заполнение поля Станция метро')
    def set_input_undeground(self):
        input_field = self.driver.find_element(*OrderButtonLocators.INPUT_UNDEGROUND)
        input_field.send_keys('Черкизовская')
        input_field.send_keys(Keys.DOWN, Keys.ENTER)

    @allure.step('Заполнение поля Телефон')
    def set_input_telephone(self, phone):
        self.driver.find_element(*OrderButtonLocators.INPUT_PHONE).send_keys(phone)

    @allure.step('Переход на форму Про аренду')
    def click_next(self):
        self.driver.find_element(*OrderButtonLocators.NEXT_BUTTON).click()

    @allure.step('Заполнение поля Когда привезти самокат')
    def set_input_bring(self, date):
        field = self.driver.find_element(*OrderButtonLocators.INPUT_BRING)
        field.send_keys(date)
        field.send_keys(Keys.ENTER)

    @allure.step('Заполнение поля Срок аренды')
    def set_input_rent(self):
        self.driver.find_element(*OrderButtonLocators.INPUT_RENT).click()
        self.wait.until(EC.element_to_be_clickable(OrderButtonLocators.CHOOSE_RENTAL_PERIOD)).click()

    @allure.step('Выбор цвета самоката - чёрный жемчуг')
    def choose_colour(self):
        self.driver.find_element(*OrderButtonLocators.CHOOSE_COLOUR_BLACK).click()

    @allure.step('Заполнение комментария')
    def set_input_comment(self, comment):
        self.driver.find_element(*OrderButtonLocators.COMMENT).send_keys(comment)
    
    @allure.step('Подтверждение заказа')
    def confirm(self):
        self.driver.find_element(*OrderButtonLocators.BUTTON_ORDER_IN_FORM).click()

    @allure.step('Нажимаем на кнопку Да. Ожидаем появления окна с сообщением об удачном оформлении заказа')
    def wait_message_success_order(self):
        self.driver.find_element(*OrderButtonLocators.CONFIRMATION_ORDER).click()
        self.wait.until(EC.visibility_of_element_located(OrderButtonLocators.SUCCESSFUL_ORDER))

    @allure.step('Кликаем по кнопке Посмотреть статус')
    def click_button_look_status(self):
        self.driver.find_element(*OrderButtonLocators.BUTTON_LOOK_STATUS).click()

    @allure.step('Кликаем на логотип Самокат в левом верхнем углу')
    def click_logo_scooter(self):
        self.driver.find_element(*OrderButtonLocators.LOGO_SCOOTER).click()

    @allure.step('Кликаем на логотип Яндекс в левом верхнем углу')
    def click_logo_yandex(self):
        self.driver.find_element(*OrderButtonLocators.LOGO_YANDEX).click()

    @allure.step('Заполняем поля формы заказа')
    def set_order_form(self, data):
        name, surname, address, telephone, date, comment = data
        self.set_input_name(name)
        self.set_input_surname(surname)
        self.set_input_adress(address)
        self.set_input_undeground()
        self.set_input_telephone(telephone)
        self.click_next()
        self.wait.until(EC.visibility_of_element_located(OrderButtonLocators.INPUT_BRING))
        self.set_input_bring(date)
        self.set_input_rent()
        self.choose_colour()
        self.set_input_comment(comment)
        self.confirm()
        self.wait_message_success_order()
    
    
    
    

    

    


    

    
    

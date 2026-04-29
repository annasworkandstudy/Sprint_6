from selenium.webdriver.common.by import By

class OrderButtonLocators:
    #Кнопки Заказать
    HEADER_ORDER_BUTTON=(By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    FOOTER_ORDER_BUTTON=(By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    #Поля для заказа
    INPUT_NAME=(By.XPATH, './/input[@placeholder="* Имя"]')
    INPUT_SURNAME=(By.XPATH, './/input[@placeholder="* Фамилия"]')
    INPUT_ADRESS=(By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    INPUT_UNDEGROUND=(By.XPATH, './/input[@placeholder="* Станция метро"]')
    INPUT_PHONE=(By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')

    #Кнопки подтверждения заказа
    ORDER_CONFIRM_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    NEXT_BUTTON=(By.XPATH, ".//button[text()='Далее']")
    CONFIRMATION_ORDER=(By.XPATH, ".//button[text()='Да']")
    BUTTON_ORDER_IN_FORM = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    #Поля для аренды
    INPUT_BRING=(By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    INPUT_RENT=(By.CLASS_NAME, "Dropdown-control")
    CHOOSE_COLOUR_BLACK=(By.XPATH, './/label[text()="чёрный жемчуг"]')
    CHOOSE_GREY_BLACK=(By.XPATH, './/label[@text()="серая безысходность"]')
    COMMENT=(By.XPATH, './/input[@placeholder="Комментарий для курьера"]')
    CHOOSE_RENTAL_PERIOD=(By.XPATH, ".//div[@class='Dropdown-menu']//div[text()='двое суток']")

    #Кнопки после успешного заказа
    SUCCESSFUL_ORDER=(By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")
    BUTTON_LOOK_STATUS = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']//button[text()='Посмотреть статус']")




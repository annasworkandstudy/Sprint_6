import allure
from pages.logo_pages import LogoPages
from selenium.webdriver.support import expected_conditions as EC

class TestLogo:
    @allure.title('Проверка перехода на главную при клике на логотип Самоката')
    def test_click_logo_scooter_open_main_page(self, driver):
        page = LogoPages(driver)
        page.push_order_button()
        page.click_logo_scooter()
        assert page.check_open_page() == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода на Дзен при клике на логотип Яндекса')
    def test_click_logo_yandex_open_dzen(self, driver):
        page = LogoPages(driver)
        page.click_logo_yandex()
        page.switch_to_next_tab()
        page.wait_url_contains("dzen.ru")
        assert "dzen.ru" in page.check_open_page()
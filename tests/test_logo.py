import allure
from pages.logo_pages import LogoPages
from selenium.webdriver.support import expected_conditions as EC

class TestLogo:
    @allure.title('Проверка перехода на главную при клике на логотип Самоката')
    def test_click_logo_scooter_open_main_page(self, driver, wait):
        page = LogoPages(driver, wait)
        page.push_order_button()
        page.click_logo_scooter()
        assert page.check_open_page() == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода на Дзен при клике на логотип Яндекса')
    def test_click_logo_yandex_open_dzen(self, driver, wait):
        page = LogoPages(driver, wait)
        page.click_logo_yandex()
        all_tabs = driver.window_handles
        driver.switch_to.window(all_tabs[1])
        wait.until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url
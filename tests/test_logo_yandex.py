from data import Urls
from locators.home_page_locators import HomePageLocators
import allure


class TestLogoYandex:

    @allure.title('Проверяем, чир при клике на лого "Яндекс" (сверху) происходит редирект на страницу Дзена в новом окне')
    def test_click_on_logo_yandex_redirect_to_dzen(self, home_page):
        home_page.get_url(Urls.HOME_PAGE_URL)
        home_page.click_on_logo_yandex()
        home_page.search_find_button()
        assert home_page.get_current_url() == Urls.DZEN_URL

    @allure.title('Проверяем, что при нажатии на лого "Самокат"- происходит возвращение на главную страницу Самоката')
    def test_click_on_scooter_logo_and_open_home_page(self, home_page, order_page):
        home_page.get_url(Urls.HOME_PAGE_URL)
        home_page.click_on_order_button(HomePageLocators.ORDER_BUTTON_UP)
        order_page.click_on_logo_scooter()
        assert home_page.get_current_url() == Urls.HOME_PAGE_URL

import pytest
from locators.home_page_locators import HomePageLocators


class TestOrderPage:

    @pytest.mark.parametrize('button, date',
                             [
                                 [HomePageLocators.ORDER_BUTTON_UP, '29.08.2024'],
                                 [HomePageLocators.ORDER_BUTTON_DOWN, '23.09.2024']
                             ]
                             )
    def test_order_scooter(self, home_page, order_page, button, date):
        home_page.click_on_cookie()
        home_page.click_on_order_button(button)
        order_page.set_data_for_whom_scooter()
        order_page.click_next_button()
        order_page.set_data_about_rent(date)
        order_page.click_on_order_then_confirm_button()
        assert order_page.check_order_is_done()

import pytest
from selenium import webdriver
from data import Urls
from pages.home_page import HomePage
from pages.order_page import OrderPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver):
    page = HomePage(driver)
    page.get_url(Urls.HOME_PAGE_URL)
    return page


@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    return page

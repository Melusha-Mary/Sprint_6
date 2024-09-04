from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
import allure


class BasePage:

    @allure.step('Загружаем драйвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загружаем страницу')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента и ожидание загрузки')
    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        element = self.find_element_and_wait(locator)
        element.click()

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_and_wait(locator)
        return element.text

    @allure.step('Ввод текста в поле')
    def set_text_to_element(self, locator, text):
        element = self.find_element_and_wait(locator)
        element.send_keys(text)

    @allure.step('Скролл страницы до нужного элемента')
    def scroll_page(self, locator):
        element = self.find_element_and_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Форматирование локатора')
    def reformate_locator(self, locator, number):
        method, locator = locator
        locator = locator.format(number)
        return method, locator

    @allure.step('Переход на вторую вкладку браузера')
    def switch_to_second_browser_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получаем url страницы')
    def get_current_url(self):
        return self.driver.current_url


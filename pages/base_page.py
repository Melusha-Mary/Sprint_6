from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_and_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_and_wait(locator)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_and_wait(locator)
        element.send_keys(text)

    def scroll_page(self, locator):
        element = self.find_element_and_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def reformate_locator(self, locator, number):
        method, locator = locator
        locator = locator.format(number)
        return method, locator

    def switch_to_second_browser_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self):
        return self.driver.current_url


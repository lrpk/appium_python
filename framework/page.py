import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class Page:
    """
        Створено основинй функціонал взаємодії зі сторінкою
    """
    def __init__(self, driver):
        self.driver = driver


    # метод для використання явних очікувань
    def wait_for_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException

# --------------------------------------------------------------------------------------------
    # def wait_for_element_to_be_clickable(self, locator, timeout=10):
    #     wait = WebDriverWait(self.driver, timeout)
    #     try:
    #         element = wait.until(EC.element_to_be_clickable(locator))
    #         return element
    #     except TimeoutException:
    #         raise TimeoutException
# --------------------------------------------------------------------------------------------

    def find_element(self, locator):
        login_button = self.wait_for_element(locator)
        return login_button

    def click_element(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    # метод перевінки наявності банера про помилку
    def banner_displayed(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

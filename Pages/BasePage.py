import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    # To create a logs (This is important)
    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('../Logs/logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # file_handler object

        logger.setLevel(logging.DEBUG)  # To skip the debug level message

        return logger

    # Custom Utilities Section

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(by_locator))
        return element.text

    def verify_link_is_present(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))
        return element

    def verify_element_is_present(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(by_locator))
        return bool(element)

    def select_option_by_text(self, by_locator, text):
        sel = Select(by_locator)
        sel.select_by_visible_text(text)

    def click_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()

    def enter_text_to_an_element(self, by_locator,text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).send_keys(text)



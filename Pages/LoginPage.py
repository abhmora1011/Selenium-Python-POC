from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BaseClass
from Test_Data.config import TestData

"""Object Repository Class"""
class LoginPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    """Locators"""
    header_banner = (By.CSS_SELECTOR, "#divLogo img")
    submit_button = (By.ID, "btnLogin")
    username = (By.ID, "txtUsername")
    password = (By.ID, "txtPassword")


    """ LOGIN SECTION """

    def verify_banner_logo_is_visible(self):
        assert self.verify_element_is_present(self.header_banner)

    def verify_username_field_is_visible(self):
        self.verify_element_is_present(self.username)

    def enter_username_data(self):
        self.enter_text(self.username,TestData.ADMIN_PASSWORD)

    def verify_password_field_is_visible(self):
        self.verify_element_is_present(self.password)

    def enter_password_data(self):
        self.enter_text(self.username, TestData.ADMIN_PASSWORD)

    def verify_button_is_visible(self):
        self.verify_element_is_present(self.submit_button)

    def submit_button_element(self):
        self.click_element_by_locator(self.submit_button)






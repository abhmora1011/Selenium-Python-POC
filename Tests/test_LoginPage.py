from Pages.LoginPage import LoginPage
from Tests.test_BaseTest import BaseTest


class Test_HomePage(BaseTest):

    def test_login_page(self):
        log_in_page = LoginPage(self.driver)
        log_in_page.verify_banner_logo_is_visible()
        log_in_page.verify_username_field_is_visible()
        log_in_page.verify_password_field_is_visible()
        log_in_page.verify_button_is_visible()
        log_in_page.enter_username_data()
        log_in_page.enter_password_data()
        log_in_page.submit_button_element()

    def test_input(self):
        self.test_login_page()











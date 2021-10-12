from Pages.LoginPage import LoginPage
from Tests.test_BaseTest import BaseTest


class Test_LoginPage(BaseTest):

    def test_login_page(self):
        log_in_page = LoginPage(self.driver)
        log_in_page.verify_banner_logo_is_visible()
        log_in_page.verify_username_field_is_visible()
        log_in_page.verify_password_field_is_visible()
        log_in_page.verify_button_is_visible()
        log_in_page.enter_username()
        log_in_page.enter_password()
        log_in_page.click_login()

    def test_input(self):
        assert "Hi" == "Hello"











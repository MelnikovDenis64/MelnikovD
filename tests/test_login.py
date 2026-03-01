import pytest
import allure
# from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage
from pages.start_page import StartPage

class TestLoginProcess:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.start_page = StartPage(self.driver)
        self.welcome_page = WelcomePage(self.driver)

    def test_login_in_account(self):
        self.start_page.open()
        self.start_page.go_to_login()
        self.login_page.login()
        self.welcome_page.logout()


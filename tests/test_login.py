import pytest
import allure
from base.base_test import BaseTest
import time


class TestLoginProcess(BaseTest):


    def test_login_in_account(self):
        self.start_page.open()
        self.start_page.go_to_login()
        self.login_page.login()
        self.welcome_page.logout()


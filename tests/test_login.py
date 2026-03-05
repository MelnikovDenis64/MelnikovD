import pytest
import allure
from base.base_test import BaseTest
import time
import allure

@pytest.mark.test_login
@allure.epic("Authorisation")
@allure.feature("Login")
class TestLoginProcess(BaseTest):

    @allure.title("Test login and logout")
    def test_login_in_account(self):
        self.start_page.open()
        self.start_page.go_to_login()
        self.login_page.login()
        self.welcome_page.logout()


from pages.login_page import LoginPage
from pages.start_page import StartPage
from pages.welcome_page import WelcomePage

class BaseTest:
    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.start_page = StartPage(self.driver)
        self.welcome_page = WelcomePage(self.driver)



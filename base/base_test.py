from pages.welcome_page import WelcomePage
from pages.login_page import LoginPage
from pages.start_page import StartPage


class BaseTest:
    def setup_method(self):
        self.login_page = LoginPage(self.driver, self.wait, self.EC)
        self.start_page = StartPage(self.driver, self.wait, self.EC)
        self.welcome_page = WelcomePage(self.driver, self.wait, self.EC)




from base.base_page import BasePage

class StartPage(BasePage):

    PAGE_URL = "https://www.freeconferencecall.com/ru"
    LOGIN_BUTTON = ("xpath", "//a[@id='login-mobile']")

    def go_to_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
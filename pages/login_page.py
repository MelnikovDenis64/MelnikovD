from base.base_page import BasePage

class LoginPage(BasePage):

    PAGE_URL = "https://www.freeconferencecall.com/ru/ru/login"
    LOGIN_INPUT = "//input[@id='login_email']"
    PASSWORD_INPUT = "//input[@id='password']"
    SEND_BUTTON = "//button[@id='loginformsubmit']"

    def login(self):
        self.driver.find_element(*self.LOGIN_INPUT).send_keys("hadentus@gmail.com")
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys("Test1234")
        self.driver.find_element(*self.SEND_BUTTON).click()
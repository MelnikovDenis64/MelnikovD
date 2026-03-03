from selenium.webdriver.common.by import By

from base.base_page import BasePage

class StartPage(BasePage):

    PAGE_URL = "https://www.freeconferencecall.com/ru"
    LOGIN_BUTTON = "//a[@id='login-desktop']"

    def go_to_login(self):
        self.wait.until(self.EC.visibility_of_element_located(self.LOGIN_BUTTON))
        self.driver.find_element(*self.LOGIN_BUTTON).click()
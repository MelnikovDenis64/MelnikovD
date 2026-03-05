from selenium.webdriver.common.by import By
import allure
from base.base_page import BasePage

class StartPage(BasePage):

    PAGE_URL = "https://www.freeconferencecall.com/ru"
    LOGIN_BUTTON = "//a[@id='login-desktop']"

    @allure.step("Go to Login page")
    def go_to_login(self):
        self.wait.until(self.EC.visibility_of_element_located(self.LOGIN_BUTTON))
        self.driver.find_element(*self.LOGIN_BUTTON).click()
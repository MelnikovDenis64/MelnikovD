from selenium.webdriver.common.by import By
import allure
from base.base_page import BasePage

class WelcomePage(BasePage):

    PAGE_URL = "https://www.freeconference.com"
    TITLE = "//h4[contains(@class, 'welcome-title')]"
    BURGER_BUTTON = "//li[@id='ember537']"
    LOGOUT_BUTTON = "//a[@title='Выйти']"

    @allure.step("Logout")
    def logout(self):
        self.wait.until(self.EC.visibility_of_element_located(self.BURGER_BUTTON))
        self.driver.find_element(*self.BURGER_BUTTON).click()
        self.wait.until(self.EC.visibility_of_element_located(self.LOGOUT_BUTTON))
        self.driver.find_element(*self.LOGOUT_BUTTON).click()


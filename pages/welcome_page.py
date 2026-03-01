from base.base_page import BasePage

class WelcomePage(BasePage):

    PAGE_URL = "https://www.freeconference.com"
    TITLE = "//h4[contains(class(), 'welcome-title')]"
    BURGER_BUTTON = "//button[contains(class(), 'navbar-toggle')]"
    LOGOUT_BUTTON = "//a[@title='Выйти']"

    def logout(self):
        self.driver.find_element(*self.BURGER_BUTTON).click()
        self.driver.find_element(*self.LOGOUT_BUTTON).click()


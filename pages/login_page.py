from base.base_page import BasePage
import allure

class LoginPage(BasePage):

    PAGE_URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = "//input[@data-test='username']"
    PASSWORD_INPUT = "//input[@data-test='password']"
    LOGIN_BUTTON = "//input[@data-test='login-button']"

    @allure.step("log in")
    def login(self):
        username_input = self.driver.find_element(*self.USERNAME_INPUT)
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        username_input.clear()
        username_input.send_keys("standard_user")
        assert username_input.get_attribute("value") == "standard_user", "Incorrect username"
        password_input.clear()
        password_input.send_keys("secret_sauce")
        assert password_input.get_attribute("value") == "secret_sauce", "Incorrect password"
        login_button.click()


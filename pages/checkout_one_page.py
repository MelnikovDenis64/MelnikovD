import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOnePage(BasePage):

    PAGE_URL = "https://www.saucedemo.com/checkout-step-one.html"
    FIRST_NAME_INPUT = "//input[@data-test='firstName']"
    LAST_NAME_INPUT = "//input[@data-test='lastName']"
    ZIP_INPUT = "//input[@data-test='postalCode']"
    CONTINUE_BUTTON = "//input[@data-test='continue']"

    @allure.step("Input client data")
    def input_client_data(self):
        first_name_input = self.driver.find_element(*self.FIRST_NAME_INPUT)
        last_name_input = self.driver.find_element(*self.LAST_NAME_INPUT)
        zip_input = self.driver.find_element(*self.ZIP_INPUT)
        continue_button = self.driver.find_element(*self.CONTINUE_BUTTON)
        first_name_input.clear()
        first_name_input.send_keys("Denis")
        assert first_name_input.get_attribute("value") == "Denis"
        last_name_input.clear()
        last_name_input.send_keys("Melnikov")
        assert last_name_input.get_attribute("value") == "Melnikov"
        zip_input.clear()
        zip_input.send_keys("123456")
        assert zip_input.get_attribute("value") == "123456"
        continue_button.click()





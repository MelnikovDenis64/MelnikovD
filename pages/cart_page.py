import allure
from base.base_page import BasePage

class CartPage(BasePage):

    PAGE_URL = "https://www.saucedemo.com/cart.html"
    CHECKOUT_BUTTON = "//button[@data-test='checkout']"
    REMOVE_BACKPACK_BUTTON = "//button[@data-test='remove-sauce-labs-backpack']"
    REMOVE_BIKE_BUTTON = "//button[@data-test='remove-sauce-labs-bike-light']"

    @allure.step("Go to checkout")
    def go_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    @allure.step("Remove all products")
    def remove_product(self):
        self.driver.find_element(*self.REMOVE_BACKPACK_BUTTON).click()
        self.driver.find_element(*self.REMOVE_BIKE_BUTTON).click()

    @allure.step("Check disabled checkout button")
    def check_disable_checkout_button(self):
        disabled_button = self.driver.find_element(*self.CHECKOUT_BUTTON).get_attribute("disabled")
        assert disabled_button is not None, "No disabled checkout button"


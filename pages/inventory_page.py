from selenium.webdriver.common.by import By
import allure
from base.base_page import BasePage

class InventoryPage(BasePage):

    PAGE_URL = "https://www.saucedemo.com/inventory.html"
    ADD_BACKPACK_PRODUCT_BUTTON = "//button[@data-test='add-to-cart-sauce-labs-backpack']"
    ADD_BIKE_PRODUCT_BUTTON = "//button[@data-test='add-to-cart-sauce-labs-bike-light']"

    @allure.step("Adding products to cart")
    def add_product(self):
        self.driver.find_element(*self.ADD_BACKPACK_PRODUCT_BUTTON).click()
        self.driver.find_element(*self.ADD_BIKE_PRODUCT_BUTTON).click()


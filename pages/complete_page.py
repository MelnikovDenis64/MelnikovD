import allure
from base.base_page import BasePage


class CompletePage(BasePage):
    PAGE_URL = "https://www.saucedemo.com/checkout-complete.html"
    BACK_HOME_BUTTON = "//button[@data-test='back-to-products']"

    @allure.step("Go to inventory page")
    def go_inventory_page(self):
        self.driver.find_element(*self.BACK_HOME_BUTTON).click()
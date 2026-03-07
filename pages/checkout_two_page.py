import allure
from base.base_page import BasePage


class CheckoutTwoPage(BasePage):
    PAGE_URL = "https://www.saucedemo.com/checkout-step-two.html"
    ITEM_TOTAL = "//div[@data-test='subtotal-label']"
    TAX = "//div[@data-test='tax-label']"
    TOTAL = "//div[@data-test='total-label']"
    FINISH_BUTTON = "//button[@data-test='finish']"

    @allure.step("Go to complete page")
    def go_to_complete(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    @allure.step("Checking the final cost calculation")
    def checking_calculation(self):
        self.driver.find_element(*self.ITEM_TOTAL).click()
        self.wait.until(self.EC.visibility_of_element_located(self.ITEM_TOTAL))
        self.wait.until(self.EC.visibility_of_element_located(self.TAX))
        self.wait.until(self.EC.visibility_of_element_located(self.TOTAL))
        item_total_float = float(self.driver.find_element(*self.ITEM_TOTAL).text[13:])
        tax_float = float(self.driver.find_element(*self.TAX).text[6:])
        total_float_fact = float(self.driver.find_element(*self.TOTAL).text[8:])
        total_float = item_total_float + tax_float
        assert total_float == total_float_fact, "Incorrect calculation"


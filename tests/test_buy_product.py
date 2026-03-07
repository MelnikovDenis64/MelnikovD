import pytest
import allure
from base.base_test import BaseTest
from allure_commons.types import Severity

@pytest.mark.feature_test
@allure.epic("Market")
@allure.feature("Product")
@allure.story("Buying product")
class TestBuyProduct(BaseTest):

    @allure.title("Positive buying process")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_positive_buy(self):
        self.login_page.open()
        self.login_page.check_page_url()
        self.login_page.login()
        self.inventory_page.check_page_url()
        self.inventory_page.add_product()
        self.inventory_page.check_product_quantity("2")
        self.inventory_page.go_cart()
        self.cart_page.check_page_url()
        self.cart_page.go_checkout()
        self.checkout_one_page.check_page_url()
        self.checkout_one_page.input_client_data()
        self.checkout_two_page.check_page_url()
        self.checkout_two_page.checking_calculation()
        self.checkout_two_page.go_to_complete()
        self.complete_page.check_page_url()
        self.complete_page.go_inventory_page()
        self.inventory_page.check_page_url()

    @allure.title("Check remove product from cart")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_remove_product(self):
        self.login_page.open()
        self.login_page.check_page_url()
        self.login_page.login()
        self.inventory_page.check_page_url()
        self.inventory_page.add_product()
        self.inventory_page.check_product_quantity("2")
        self.inventory_page.go_cart()
        self.cart_page.check_page_url()
        self.cart_page.remove_product()
        self.cart_page.check_none_quantity_element()
        self.cart_page.check_disable_checkout_button()





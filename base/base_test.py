from pages.login_page import LoginPage
from pages.checkout_one_page import CheckoutOnePage
from pages.checkout_two_page import CheckoutTwoPage
from pages.cart_page import CartPage
from pages.complete_page import CompletePage
from pages.inventory_page import InventoryPage

class BaseTest:
    def setup_method(self):
        self.login_page = LoginPage(self.driver, self.wait, self.EC)
        self.checkout_one_page = CheckoutOnePage(self.driver, self.wait, self.EC)
        self.checkout_two_page = CheckoutTwoPage(self.driver, self.wait, self.EC)
        self.cart_page = CartPage(self.driver, self.wait, self.EC)
        self.complete_page = CompletePage(self.driver, self.wait, self.EC)
        self.inventory_page = InventoryPage(self.driver, self.wait, self.EC)



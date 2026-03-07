from selenium.webdriver.chrome.webdriver import WebDriver
from metaclasses.meta_locator import MetaLocator
import allure
from utils.generators import Generators

class BasePage(metaclass=MetaLocator):
    CART = "//a[@class='shopping_cart_link']"
    PRODUCT_COUNT = "//span[@data-test='shopping-cart-badge']"

    def __init__(self, driver, wait, EC):
        self.driver : WebDriver = driver
        self.wait = wait
        self.EC = EC
        self.generators = Generators()

    @allure.step("Open page")
    def open(self):
        self.driver.get(self.PAGE_URL)

    @allure.step("Go to cart")
    def go_cart(self):
        self.driver.find_element(*self.CART).click()

    @allure.step("Check product count")
    def check_product_quantity(self, quantity):
        product_count = self.driver.find_element(*self.PRODUCT_COUNT).text
        assert product_count == quantity, "Incorrect quantity of items in the cart"

    @allure.step("Checking if there are any products in the cart")
    def check_none_quantity_element(self):
        assert self.wait.until(self.EC.invisibility_of_element_located(self.PRODUCT_COUNT)), "Availability of products in the cart"

    @allure.step("Check page url")
    def check_page_url(self):
        current_url = self.driver.current_url
        assert current_url == self.PAGE_URL, "Incorrect url"




from selenium.webdriver.chrome.webdriver import WebDriver
from metaclasses.meta_locator import MetaLocator
import allure
from utils.generators import Generators

class BasePage(metaclass=MetaLocator):

    LOGO = "//a[@class='fcc-logo']"


    def __init__(self, driver, wait, EC):
        self.driver : WebDriver = driver
        self.wait = wait
        self.EC = EC
        self.generators = Generators()

    @allure.step("Open page")
    def open(self):
        self.driver.get(self.PAGE_URL)

    @allure.step("Logo click")
    def logo_click(self):
        self.driver.find_element(*self.LOGO).click()

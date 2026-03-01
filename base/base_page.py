from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from metaclasses.meta_locator import MetaLocator


class BasePage:

    LOGO = "//a[@class='fcc-logo']"


    def __init__(self, driver):
        self.driver : WebDriver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)

    def logo_click(self):
        self.driver.find_element(*self.LOGO).click()

# for Lesson 7 use

import json
from selenium.webdriver.chrome.webdriver import WebDriver

class CookieManager:
    def __init__(self, driver, file_path="cookies.json"):
        self.driver : WebDriver = driver
        self.file_path = file_path

    def save_cookies(self):
        cookies = self.driver.get_cookies()
        with open(self.file_path, "w") as file:
            json.dump(cookies, file, indent=4)

    def load_cookies(self):
        self.driver.delete_all_cookies()
        with open(self.file_path, "r") as file:
            cookies = json.load(file)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

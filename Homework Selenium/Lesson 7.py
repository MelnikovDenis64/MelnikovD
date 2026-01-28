import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cookies_manager import CookieManager

options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)
cookies_manager = CookieManager(driver)

driver.get("https://www.freeconferencecall.com/ru/ru/login")

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
COMPLETE_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

if os.path.exists("cookies.json"):
    cookies_manager.load_cookies()
else:
    driver.find_element(*LOGIN_FIELD).send_keys("***@gmail.com")
    driver.find_element(*PASSWORD_FIELD).send_keys("Test1234")
    driver.find_element(*COMPLETE_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='grid-row']")))
    cookies_manager.save_cookies()


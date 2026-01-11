import time
from selenium import webdriver
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()

options.add_argument("--headless=new")
options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--window-size=1366,768")
options.add_argument("--disable-cache")
options.add_argument("--no-sandbox")
options.page_load_strategy = "eager"

driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/upload-download")
input_file = driver.find_element('xpath', '//input[@id="uploadFile"]')
input_file.send_keys(r"C:\Users\dVmelnikov\Desktop\photo_2024-09-17_13-47-06.jpg")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")

NON_CLICKABLE_5_SECONDS = ("xpath", "//button[@id='enableAfter']")
wait.until(EC.element_to_be_clickable(NON_CLICKABLE_5_SECONDS))
driver.find_element(By.XPATH, "//button[@id='enableAfter']").click()

VISIBLE_AFTER_5_SECONDS = ("xpath", "//button[@id='visibleAfter']")
wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_5_SECONDS))
driver.find_element(By.XPATH, "//button[@id='visibleAfter']").click()




driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[@id='enableAfter']").click()


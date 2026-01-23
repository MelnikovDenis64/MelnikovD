import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# Отключение видимости webdriver mode:
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# Кастомный юзер-агент:
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36")

options.page_load_strategy = "eager"
driver = webdriver.Chrome(options=options)

#Проверим юзер-агент:
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
time.sleep(5)


# Работа с алертами:
wait = WebDriverWait(driver, 10, poll_frequency=1)
driver.get("https://demoqa.com/alerts")

driver.find_element(By.XPATH, "//button[@id='alertButton']").click()
wait.until(EC.alert_is_present())
driver.switch_to.alert.accept()

driver.find_element(By.XPATH, "//button[@id='timerAlertButton']").click()
wait.until(EC.alert_is_present())
driver.switch_to.alert.accept()

driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
wait.until(EC.alert_is_present())
driver.switch_to.alert.dismiss()

driver.find_element(By.XPATH, "//button[@id='promtButton']").click()
wait.until(EC.alert_is_present())
driver.switch_to.alert.send_keys("Denis")
driver.switch_to.alert.accept()

time.sleep(5)

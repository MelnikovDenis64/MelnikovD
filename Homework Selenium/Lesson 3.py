from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

user_name_input = driver.find_element("xpath", "//input[@id='userName']")
user_name_input.clear()
user_name_input.send_keys("Denis")
assert user_name_input.get_attribute("value") == "Denis"

user_email_input = driver.find_element("xpath", "//input[@id='userEmail']")
user_email_input.clear()
user_email_input.send_keys("Denis@mail.com")
assert user_email_input.get_attribute("value") == "Denis@mail.com"

current_address_input = driver.find_element("xpath", "//textarea[@id='currentAddress']")
current_address_input.clear()
current_address_input.send_keys("Saratov, Volskaya str., 10 house")
assert current_address_input.get_attribute("value") == "Saratov, Volskaya str., 10 house"

permanent_address_input = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
permanent_address_input.clear()

permanent_address_input.send_keys("Saratov, Volskaya str., 10 house")
permanent_address_input.send_keys(Keys.CONTROL + "A")
permanent_address_input.send_keys(Keys.BACKSPACE)
assert permanent_address_input.get_attribute("value") == "", "Поле \"Постоянный адрес\" не очистилось"

permanent_address_input.send_keys("Saratov, Volskaya str., 19 house")
assert permanent_address_input.get_attribute("value") == "Saratov, Volskaya str., 19 house"

submit_button = driver.find_element("xpath", "//button[@id='submit']")
submit_button.click()


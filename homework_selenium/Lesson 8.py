import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/checkbox")

CHECKBOX_ELEMENT = ('xpath', '//label[@for="tree-node-home"]')
driver.find_element(*CHECKBOX_ELEMENT).click()
time.sleep(1)

driver.get("https://demoqa.com/radio-button")
BUTTON_ELEMENT_YES = ('xpath', '//input[@id="yesRadio"]')
BUTTON_ELEMENT_NO = ('xpath', '//input[@id="noRadio"]')
BUTTON_LABEL_YES = ('xpath', '//label[@for="yesRadio"]')
driver.find_element(*BUTTON_LABEL_YES).click()
radio_button_selected = driver.find_element(*BUTTON_ELEMENT_YES).is_selected()
assert radio_button_selected == True, "radio_button_yes не выбрана"
radio_button_enabled = driver.find_element(*BUTTON_ELEMENT_NO).is_enabled()
assert radio_button_enabled == False, "radio_button_no доступна"
time.sleep(1)


driver.get("https://demoqa.com/select-menu")

INPUT_VALUE_DROPDOWN = ('xpath', '//input[@id="react-select-2-input"]')
SELECT_VALUE_DROPDOWN = ('xpath', '//select[@id="oldSelectMenu"]')
MULTISELECT_DROPDOWN = ('xpath', '//input[@id="react-select-4-input"]')

driver.find_element(*INPUT_VALUE_DROPDOWN).send_keys("Group 1, option 1")
driver.find_element(*INPUT_VALUE_DROPDOWN).send_keys(Keys.ENTER)
time.sleep(1)

DROPDOWN = Select(driver.find_element(*SELECT_VALUE_DROPDOWN))
DROPDOWN.select_by_index(2)
time.sleep(1)
DROPDOWN.select_by_visible_text("Blue")
time.sleep(1)
DROPDOWN.select_by_value("6")
time.sleep(1)
dropdown_value = driver.find_element(*SELECT_VALUE_DROPDOWN).get_attribute("value")
assert dropdown_value == "6", "Значение не выбрано"

driver.find_element(*MULTISELECT_DROPDOWN).send_keys("Green")
driver.find_element(*MULTISELECT_DROPDOWN).send_keys(Keys.ENTER)
driver.find_element(*MULTISELECT_DROPDOWN).send_keys("Blue")
driver.find_element(*MULTISELECT_DROPDOWN).send_keys(Keys.ENTER)
driver.find_element(*MULTISELECT_DROPDOWN).send_keys(Keys.ESCAPE)
time.sleep(1)
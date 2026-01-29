import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument("----window-size=1920,1080")
driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)

driver.get("https://demoqa.com/buttons")

DOUBLE_CLICK = driver.find_element('xpath', '//button[@id="doubleClickBtn"]')
RIGHT_CLICK = driver.find_element('xpath', '//button[@id="rightClickBtn"]')
ONE_CLICK = driver.find_element('xpath', '//button[text()="Click Me"]')

actions.double_click(DOUBLE_CLICK).perform()
actions.context_click(RIGHT_CLICK).perform()
actions.click(ONE_CLICK).perform()
time.sleep(1)


driver.get("https://demoqa.com/menu#")

MAIN_ITEM = driver.find_element('xpath', '//a[text()="Main Item 2"]')
SUB_LIST = driver.find_element('xpath', '//a[text()="SUB SUB LIST »"]')
SUB_ITEM = driver.find_element('xpath', '//a[text()="Sub Sub Item 2"]')

actions.move_to_element(MAIN_ITEM).pause(3).move_to_element(SUB_LIST).pause(3).move_to_element(SUB_ITEM).pause(3).perform()



driver.get("https://demoqa.com/droppable")

wait = WebDriverWait(driver, 10, poll_frequency=1)

source = ('xpath', '//div[@id="draggable"]')

wait.until(EC.visibility_of_element_located(source))
SOURCE = driver.find_element('xpath', '//div[@id="draggable"]')
TARGET = driver.find_element('xpath', '//div[@id="droppable"]')

actions.drag_and_drop(SOURCE, TARGET).pause(2).perform()
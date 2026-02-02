from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.saucedemo.com")

USERNAME_INPUT = driver.find_element(By.XPATH, "//input[@data-test='username']")
PASSWORD_INPUT = driver.find_element(By.XPATH, "//input[@data-test='password']")
LOGIN_BUTTON = driver.find_element(By.XPATH, "//input[@data-test='login-button']")

USERNAME_INPUT.send_keys("standard_user")
PASSWORD_INPUT.send_keys("secret_sauce")
LOGIN_BUTTON.click()

current_url = driver.current_url
current_title = driver.title
assert current_url == "https://www.saucedemo.com/inventory.html" and current_title == "Swag Labs", "Переход на неверную страницу"

ADD_FIRST_PRODUCT_BUTTON = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
ITEM_PRICE = driver.find_element(By.XPATH, "//div[@data-test='inventory-item-price']")
CART_TRANSITION_BUTTON = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")

item_price = ITEM_PRICE.text
ADD_FIRST_PRODUCT_BUTTON.click()
CART_TRANSITION_BUTTON.click()

current_url = driver.current_url
current_title = driver.title
assert current_url == "https://www.saucedemo.com/cart.html" and current_title == "Swag Labs", "Переход на неверную страницу"

CHECKOUT_BUTTON = driver.find_element(By.XPATH, "//button[@data-test='checkout']")
CHECKOUT_BUTTON.click()

current_url = driver.current_url
current_title = driver.title
assert current_url == "https://www.saucedemo.com/checkout-step-one.html" and current_title == "Swag Labs", "Переход на неверную страницу"

FIRST_NAME_INPUT = driver.find_element(By.XPATH, "//input[@data-test='firstName']")
LAST_NAME_INPUT = driver.find_element(By.XPATH, "//input[@data-test='lastName']")
ZIP_INPUT = driver.find_element(By.XPATH, "//input[@data-test='postalCode']")
CONTINUE_BUTTON = driver.find_element(By.XPATH, "//input[@data-test='continue']")

FIRST_NAME_INPUT.send_keys("Denis")
LAST_NAME_INPUT.send_keys("Melnikov")
ZIP_INPUT.send_keys("413100")
CONTINUE_BUTTON.click()

ITEM_TOTAL = ("xpath", "//div[@data-test='subtotal-label']")
wait.until(EC.visibility_of_element_located(ITEM_TOTAL))
item_total = driver.find_element(By.XPATH, "//div[@data-test='subtotal-label']").text
current_url = driver.current_url
current_title = driver.title
assert item_price in item_total, "Цена на витрине не соответствует цене в корзине"
assert current_url == "https://www.saucedemo.com/checkout-step-two.html" and current_title == "Swag Labs", "Переход на неверную страницу"

FINISH_BUTTON = driver.find_element(By.XPATH, "//button[@data-test='finish']")
FINISH_BUTTON.click()

current_url = driver.current_url
current_title = driver.title
complete_header_text = driver.find_element(By.XPATH, "//h2[@data-test='complete-header']").text
assert item_price in item_total, "Цена на витрине не соответствует цене в корзине"
assert current_url == "https://www.saucedemo.com/checkout-complete.html" and current_title == "Swag Labs", "Переход на неверную страницу"
assert complete_header_text == "Thank you for your order!", "Неверный заголовок успешного экрана"

BACK_HOME_BUTTON = driver.find_element(By.XPATH, "//button[@data-test='back-to-products']")
BACK_HOME_BUTTON.click()

current_url = driver.current_url
current_title = driver.title
assert current_url == "https://www.saucedemo.com/inventory.html" and current_title == "Swag Labs", "Переход на неверную страницу"
import time
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
wait = WebDriverWait(driver, 5, poll_frequency=0.5)
driver.get("https://www.saucedemo.com")

# Экран Авторизации
USERNAME_INPUT = driver.find_element(By.XPATH, "//input[@data-test='username']")
PASSWORD_INPUT = driver.find_element(By.XPATH, "//input[@data-test='password']")
LOGIN_BUTTON = driver.find_element(By.XPATH, "//input[@data-test='login-button']")

time.sleep(1)

USERNAME_INPUT.clear()
USERNAME_INPUT.send_keys("standard_user")
assert USERNAME_INPUT.get_attribute("value") == 'standard_user'
USERNAME_INPUT.clear()
PASSWORD_INPUT.send_keys("secret_sauce")
assert PASSWORD_INPUT.get_attribute("value") == 'secret_sauce'
LOGIN_BUTTON.click()

# Экран Витрины
current_url = driver.current_url
current_title = driver.title
assert current_url == "https://www.saucedemo.com/inventory.html" and current_title == "Swag Labs", "Переход на неверную страницу"

ADD_BACKPACK_PRODUCT_BUTTON = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
ADD_BIKE_PRODUCT_BUTTON = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bike-light']")
CART_TRANSITION_BUTTON = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")

time.sleep(1)

ADD_BACKPACK_PRODUCT_BUTTON.click()
ADD_BIKE_PRODUCT_BUTTON.click()

PRODUCT_COUNT = driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']")
assert PRODUCT_COUNT.text == "2", "Неверное кол-во товаров в корзине"

time.sleep(1)

CART_TRANSITION_BUTTON.click()

# Экран Корзины
current_url = driver.current_url
current_title = driver.title
assert current_url == "https://www.saucedemo.com/cart.html" and current_title == "Swag Labs", "Переход на неверную страницу"

time.sleep(1)

CHECKOUT_BUTTON = driver.find_element(By.XPATH, "//button[@data-test='checkout']")
CHECKOUT_BUTTON.click()

# Экран 1 шага оформления заказа (Ввод ФИ и Индекса)
current_url = driver.current_url
current_title = driver.title
assert current_url == "https://www.saucedemo.com/checkout-step-one.html" and current_title == "Swag Labs", "Переход на неверную страницу"

FIRST_NAME_INPUT = driver.find_element(By.XPATH, "//input[@data-test='firstName']")
LAST_NAME_INPUT = driver.find_element(By.XPATH, "//input[@data-test='lastName']")
ZIP_INPUT = driver.find_element(By.XPATH, "//input[@data-test='postalCode']")
CONTINUE_BUTTON = driver.find_element(By.XPATH, "//input[@data-test='continue']")

FIRST_NAME_INPUT.clear()
FIRST_NAME_INPUT.send_keys("Denis")
assert FIRST_NAME_INPUT.get_attribute("value") == 'Denis'
LAST_NAME_INPUT.clear()
LAST_NAME_INPUT.send_keys("Melnikov")
assert LAST_NAME_INPUT.get_attribute("value") == 'Melnikov'
ZIP_INPUT.clear()
ZIP_INPUT.send_keys("413100")
assert ZIP_INPUT.get_attribute("value") == '413100'

time.sleep(1)

CONTINUE_BUTTON.click()

time.sleep(1)

# Экран подтверждения заказа и расчета итоговой стоимости
current_url = driver.current_url
current_title = driver.title
assert current_url == "https://www.saucedemo.com/checkout-step-two.html" and current_title == "Swag Labs", "Переход на неверную страницу"

ITEM_TOTAL = ("xpath", "//div[@data-test='subtotal-label']")
TAX = ("xpath", "//div[@data-test='tax-label']")
TOTAL = ("xpath", "//div[@data-test='total-label']")
wait.until(EC.visibility_of_element_located(ITEM_TOTAL))
wait.until(EC.visibility_of_element_located(TAX))
wait.until(EC.visibility_of_element_located(TOTAL))
item_total_float = float(driver.find_element(*ITEM_TOTAL).text[13:])
tax_float = float(driver.find_element(*TAX).text[6:])
total_float_fact = float(driver.find_element(*TOTAL).text[8:])
total_float = item_total_float + tax_float
assert total_float == total_float_fact, "Некорректный расчет итоговой стоимости"

FINISH_BUTTON = driver.find_element(By.XPATH, "//button[@data-test='finish']")
FINISH_BUTTON.click()

time.sleep(1)

# Финальный экран успешной отправки заявки
current_url = driver.current_url
current_title = driver.title
assert current_url == "https://www.saucedemo.com/checkout-complete.html" and current_title == "Swag Labs", "Переход на неверную страницу"
complete_header_text = driver.find_element(By.XPATH, "//h2[@data-test='complete-header']").text
assert complete_header_text == "Thank you for your order!", "Неверный заголовок успешного экрана"

BACK_HOME_BUTTON = driver.find_element(By.XPATH, "//button[@data-test='back-to-products']")
BACK_HOME_BUTTON.click()

time.sleep(1)

# Возврат на Витрину
current_url = driver.current_url
current_title = driver.title
assert current_url == "https://www.saucedemo.com/inventory.html" and current_title == "Swag Labs", "Переход на неверную страницу"
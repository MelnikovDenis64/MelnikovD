import pytest
import allure
import time
from selenium.webdriver.common.by import By
from allure_commons.types import Severity
from allure_commons.types import AttachmentType

@pytest.mark.feature_test
@allure.epic("Market")
@allure.feature("Product")
@allure.story("Buying product")
class TestBuyProduct:
    @allure.title("Buying process")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_buy_product(self):
        with allure.step("Open page Login"):
            self.driver.get("https://www.saucedemo.com")

            # Экран Авторизации
            USERNAME_INPUT = self.driver.find_element(By.XPATH, "//input[@data-test='username']")
            PASSWORD_INPUT = self.driver.find_element(By.XPATH, "//input[@data-test='password']")
            LOGIN_BUTTON = self.driver.find_element(By.XPATH, "//input[@data-test='login-button']")
            time.sleep(1)

        with allure.step("Input user credentials"):

            USERNAME_INPUT.clear()
            USERNAME_INPUT.send_keys("standard_user")
            assert USERNAME_INPUT.get_attribute("value") == 'standard_user'
            USERNAME_INPUT.clear()
            PASSWORD_INPUT.send_keys("secret_sauce")
            assert PASSWORD_INPUT.get_attribute("value") == 'secret_sauce'
            LOGIN_BUTTON.click()

        with allure.step("Assert page url (inventory)"):
            # Экран Витрины
            current_url = self.driver.current_url
            current_title = self.driver.title
            assert current_url == "https://www.saucedemo.com/inventory.html" and current_title == "Swag Labs", "Переход на неверную страницу"

        with allure.step("Adding products to cart"):
            ADD_BACKPACK_PRODUCT_BUTTON = self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
            ADD_BIKE_PRODUCT_BUTTON = self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bike-light']")
            CART_TRANSITION_BUTTON = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
            time.sleep(1)
            ADD_BACKPACK_PRODUCT_BUTTON.click()
            ADD_BIKE_PRODUCT_BUTTON.click()

        with allure.step("Checking the quantity of items in the cart"):
            PRODUCT_COUNT = self.driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']")
            assert PRODUCT_COUNT.text == "2", "Неверное кол-во товаров в корзине"
            time.sleep(1)

        with allure.step("Go to cart"):
            CART_TRANSITION_BUTTON.click()

        with allure.step("Assert page url (cart)"):
            # Экран Корзины
            current_url = self.driver.current_url
            current_title = self.driver.title
            assert current_url == "https://www.saucedemo.com/cart.html" and current_title == "Swag Labs", "Переход на неверную страницу"
            time.sleep(1)

        with allure.step("Go to checkout"):
            CHECKOUT_BUTTON = self.driver.find_element(By.XPATH, "//button[@data-test='checkout']")
            CHECKOUT_BUTTON.click()

        with allure.step("Assert page url (checkout-step-one)"):
            # Экран 1 шага оформления заказа (Ввод ФИ и Индекса)
            current_url = self.driver.current_url
            current_title = self.driver.title
            assert current_url == "https://www.saucedemo.com/checkout-step-one.html" and current_title == "Swag Labs", "Переход на неверную страницу"

        with allure.step("Input client data"):
            FIRST_NAME_INPUT = self.driver.find_element(By.XPATH, "//input[@data-test='firstName']")
            LAST_NAME_INPUT = self.driver.find_element(By.XPATH, "//input[@data-test='lastName']")
            ZIP_INPUT = self.driver.find_element(By.XPATH, "//input[@data-test='postalCode']")
            CONTINUE_BUTTON = self.driver.find_element(By.XPATH, "//input[@data-test='continue']")

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

        with allure.step("Assert page url (checkout-step-two)"):
            # Экран подтверждения заказа и расчета итоговой стоимости
            current_url = self.driver.current_url
            current_title = self.driver.title
            assert current_url == "https://www.saucedemo.com/checkout-step-two.html" and current_title == "Swag Labs", "Переход на неверную страницу"

        with allure.step("Checking the final cost calculation"):
            ITEM_TOTAL = ("xpath", "//div[@data-test='subtotal-label']")
            TAX = ("xpath", "//div[@data-test='tax-label']")
            TOTAL = ("xpath", "//div[@data-test='total-label']")
            self.wait.until(self.EC.visibility_of_element_located(ITEM_TOTAL))
            self.wait.until(self.EC.visibility_of_element_located(TAX))
            self.wait.until(self.EC.visibility_of_element_located(TOTAL))
            item_total_float = float(self.driver.find_element(*ITEM_TOTAL).text[13:])
            tax_float = float(self.driver.find_element(*TAX).text[6:])
            total_float_fact = float(self.driver.find_element(*TOTAL).text[8:])
            total_float = item_total_float + tax_float
            assert total_float == total_float_fact, "Некорректный расчет итоговой стоимости"

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            allure.attach(name="final cost calculation",
                          body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG
            )


        with allure.step("Go to complete page"):
            FINISH_BUTTON = self.driver.find_element(By.XPATH, "//button[@data-test='finish']")
            FINISH_BUTTON.click()
            time.sleep(1)

        with allure.step("Assert page url (heckout-complete)"):
            # Финальный экран успешной отправки заявки
            current_url = self.driver.current_url
            current_title = self.driver.title
            assert current_url == "https://www.saucedemo.com/checkout-complete.html" and current_title == "Swag Labs", "Переход на неверную страницу"
            complete_header_text = self.driver.find_element(By.XPATH, "//h2[@data-test='complete-header']").text
            assert complete_header_text == "Thank you for your order!", "Неверный заголовок успешного экрана"

        with allure.step("Go to homepage"):
            BACK_HOME_BUTTON = self.driver.find_element(By.XPATH, "//button[@data-test='back-to-products']")
            BACK_HOME_BUTTON.click()
            time.sleep(1)

        with allure.step("Assert page url (inventory)"):
            # Возврат на Витрину
            current_url = self.driver.current_url
            current_title = self.driver.title
            assert current_url == "https://www.saucedemo.com/inventory.html" and current_title == "Swag Labs", "Переход на неверную страницу"
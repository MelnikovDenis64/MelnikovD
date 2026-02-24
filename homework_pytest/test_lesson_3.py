import time
import pytest
from selenium.webdriver.common.by import By

class TestExample2:

    @pytest.mark.usefixtures('request_example')
    @pytest.mark.test_1
    def test_print_info(self):
        print(self.name)
        print(self.email)

    @pytest.mark.test_2
    def test_input_field(self, driver):
        driver.get("https://www.saucedemo.com")

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



    @pytest.mark.test_3
    def test_print_namedtuple(self, generate_user_data_namedtuple):
        login = generate_user_data_namedtuple.login
        password = generate_user_data_namedtuple.password
        email = generate_user_data_namedtuple.email
        first_name = generate_user_data_namedtuple.first_name
        last_name = generate_user_data_namedtuple.last_name
        print(f"""
            {login}, 
            {password}, 
            {email}, 
            {first_name}, 
            {last_name}""")


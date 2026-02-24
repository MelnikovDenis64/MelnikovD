import time
import pytest
from selenium import webdriver


class TestExample:

    USERNAME = ('xpath', '//input[@id="userName"]')
    EMAIL = ('xpath', '//input[@id="userEmail"]')
    ADDRESS_CURR = ('xpath', '//textarea[@id="currentAddress"]')
    ADDRESS_PERM = ('xpath', '//textarea[@id="permanentAddress"]')
    BUTTON = ('xpath', '//button[@id="submit"]')
    OUTPUT = ('xpath', '//div[@id="output"]')

    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument('window-size=1900x1080')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://demoqa.com/text-box")

    @pytest.mark.smoke
    def test_url(self):
        assert self.driver.current_url == "https://demoqa.com/text-box", 'Неверный url'

    @pytest.mark.regress
    def test_input_field(self):
        time.sleep(2)
        self.driver.find_element(*self.USERNAME).send_keys('Denis')
        self.driver.find_element(*self.EMAIL).send_keys('Denis@mail.com')
        self.driver.find_element(*self.ADDRESS_CURR).send_keys('Test1234')
        self.driver.find_element(*self.ADDRESS_PERM).send_keys('Test1234')
        self.driver.find_element(*self.BUTTON).click()
        assert "Denis" in self.driver.find_element(*self.OUTPUT).text, 'Нет сохранения инпутов'

    def teardown_method(self):
        self.driver.quit()



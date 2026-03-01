import os

import pytest
from selenium import webdriver
from collections import namedtuple
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver(request):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    request.cls.wait = wait
    request.cls.driver = driver
    request.cls.EC = EC
    yield
    driver.quit()



@pytest.fixture()
def setup_environment_properties():
    properties = {
        "STAGE": os.environ["STAGE"],
        "BROWSER": os.environ["BROWSER"],
        "OS": os.environ["OS"]
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")




@pytest.fixture
def generate_user_data_namedtuple():
    fake = Faker()
    UserNew = namedtuple(
        'UserData', ['login', 'password', 'email', 'first_name', 'last_name'])
    return UserNew(fake.email(), fake.password(), fake.email(), fake.first_name(), fake.last_name())


@pytest.fixture(name='request_example')
def generate_user_data_request(request):
    fake = Faker()
    request.cls.name = fake.name()
    request.cls.email = fake.email()



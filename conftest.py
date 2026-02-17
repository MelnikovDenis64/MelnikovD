import pytest
from collections import namedtuple
from faker import Faker

@pytest.fixture
def driver():
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    return driver

@pytest.fixture
def generate_user_data_namedtuple():
    fake = Faker()
    UserNew = namedtuple(
        'UserData', ['login', 'password', 'email', 'first_name', 'last_name'])
    user = UserNew(fake.email(), fake.password(), fake.email(), fake.first_name(), fake.last_name())
    return user

@pytest.fixture(name='request_example')
def generate_user_data_request(request):
    fake = Faker()
    request.cls.name = fake.name()
    request.cls.email = fake.email()



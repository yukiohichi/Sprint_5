import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker
from pages.registration_page import RegistrationPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get('https://qa-desk.stand.praktikum-services.ru/')
    yield driver
    driver.quit()

@pytest.fixture
def email():
    fake = Faker()
    return fake.email()

@pytest.fixture
def password():
    fake = Faker()
    return fake.password(length=10)

@pytest.fixture
def name():
    fake = Faker()
    return fake.name()

@pytest.fixture
def text_description():
    fake = Faker()
    return fake.text()

@pytest.fixture
def price():
    fake = Faker()
    return fake.random_int(min=100, max=9999)

@pytest.fixture
def user(driver, email, password):
    page = RegistrationPage(driver)

    page.click_auth_button()
    page.wait_for_account_button()
    page.click_account_button()

    page.wait_for_email()
    page.enter_email(email)
    page.enter_password(password)
    page.enter_confirm_password(password)
    page.click_register_button()

    page.wait_for_user_avatar()
    page.click_exit_button()

    return email, password
import pytest
from selenium import webdriver
from pages.registration_page import RegistrationPage
from selenium.webdriver.chrome.options import Options
from pages.eco_page import EcoPage
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    edge_driver = webdriver.Chrome(options=options)
    edge_driver.maximize_window()
    return edge_driver


@pytest.fixture()
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture()
def eco_page(driver):
    return EcoPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)

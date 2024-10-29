import pytest
from selenium import webdriver
from pages.registration_page import RegistrationPage
from pages.eco_page import EcoPage
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    edge_driver = webdriver.Edge()
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

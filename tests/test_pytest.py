from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests_selenium.scraping_selenium import initialize_driver, get_title, get_page, get_current_url, get_product_price

@pytest.fixture
def driver():
    driver = initialize_driver()
    yield driver
    driver.quit()

def test_get_page(driver):
    get_page(driver, "https://demowebshop.tricentis.com/blue-jeans")
    assert "https://demowebshop.tricentis.com/blue-jeans" == get_current_url(driver)

def test_get_title(driver):
    get_page(driver, "https://demowebshop.tricentis.com/blue-jeans")
    assert "Demo Web Shop. Blue Jeans" == get_title(driver)

def test_get_product_price(driver):
    get_page(driver, "https://demowebshop.tricentis.com/blue-jeans")
    price = get_product_price(driver)
    assert price == "1.00"

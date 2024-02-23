from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def initialize_driver():
    return webdriver.Chrome()

def get_page(driver, url):
    driver.get(url)
    time.sleep(2)

def get_title(driver):
    return driver.title

def get_current_url(driver):
    return driver.current_url

def get_image_source(driver, image_id):
    image_element = driver.find_element(By.ID, image_id)
    return image_element.get_attribute("src")

def get_element_text(driver, by_method, identifier):
    element = driver.find_element(by_method, identifier)
    return element.get_attribute("innerText")

def get_product_price(driver):
    price_element = driver.find_element(By.CLASS_NAME, "price-value-36")
    return price_element.get_attribute("innerText")
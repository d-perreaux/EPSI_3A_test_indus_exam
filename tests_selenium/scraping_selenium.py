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

def get_image_source(driver):
    image_element = driver.find_element(By.ID, 'main-product-img-36')
    return image_element.get_attribute("src")

def get_element_article(driver):
    element = driver.find_element(By.TAG_NAME, 'h1')
    return element.get_attribute("innerText")

def get_product_price(driver):
    price_element = driver.find_element(By.CLASS_NAME, "price-value-36")
    return price_element.get_attribute("innerText")


if __name__ == '__main__':
    driver = initialize_driver()
    get_page(driver, 'https://demowebshop.tricentis.com/blue-jeans')
    print("Titre:", get_title(driver))
    print("URL:", get_current_url(driver))
    print("Image Source:", get_image_source(driver))
    print("Prix:", get_product_price(driver))
    print("Element article:", get_element_article(driver))

    
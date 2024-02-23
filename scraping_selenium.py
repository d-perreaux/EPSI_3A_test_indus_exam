from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://demowebshop.tricentis.com/blue-jeans')
time.sleep(2)
title = driver.title
print(title)
url = driver.current_url
print(url)
product_form = driver.find_element(By.ID, "product-details-form")
print(product_form.get_attribute("action"))
print(product_form.get_attribute("method"))
image_jean = driver.find_element(By.ID, "main-product-img-36")
print(image_jean.get_attribute("src"))
price = driver.find_element(By.CLASS_NAME, "price-value-36")
print(price.get_attribute("innerText"))
stock = driver.find_element(By.CLASS_NAME, "value")
print(stock.get_attribute("innerText"))
h1 = driver.find_element(By.TAG_NAME, "h1")
print(h1.get_attribute("innerText"))
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

driver = webdriver.Chrome('D:/Téléchargements/chromedriver_win32')
driver.get('https://demowebshop.tricentis.com/')
web = driver.maximize_window()
time.sleep(5)
print("Ouvre URL et Agrandir")
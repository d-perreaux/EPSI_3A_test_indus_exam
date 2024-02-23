import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestExamenIndustrialisation():
  def setup_method(self, method):
    chrome_options = webdriver.ChromeOptions()
    self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_examenIndustrialisation(self):
    self.driver.get("https://demowebshop.tricentis.com/")
    self.driver.set_window_size(1239, 1002)
    element = self.driver.find_element(By.LINK_TEXT, "Register")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Register").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    time.sleep(2)
    actions.move_to_element(element).perform()
    time.sleep(2)
    self.driver.find_element(By.ID, "gender-male").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "FirstName").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "FirstName").send_keys("MENDELATHUNE")
    time.sleep(2)
    self.driver.find_element(By.ID, "LastName").send_keys("Gerard")
    time.sleep(2)
    self.driver.find_element(By.ID, "Email").send_keys("gerard.mendelathune@euro.dol")
    time.sleep(2)
    self.driver.find_element(By.ID, "Password").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "Password").send_keys("thunedol")
    time.sleep(2)
    self.driver.find_element(By.ID, "ConfirmPassword").send_keys("thunedol")
    time.sleep(2)
    self.driver.find_element(By.ID, "register-button").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "small-searchterms").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "small-searchterms").send_keys("jeans")
    time.sleep(2)
    self.driver.find_element(By.ID, "small-searchterms").send_keys(Keys.ENTER)
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Blue Jeans").click()


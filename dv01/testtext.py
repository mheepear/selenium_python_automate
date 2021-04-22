import pytest
import time
import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

class TestKycandy():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  # def teardown_method(self, method):
  #   self.driver.quit()
  
  def test_kycandy(self):
    webdriver.Firefox().get("http://portal.dev.getzense.com/")
    # wait for element and click #
    ##############################
    test = self.driver.title
    self assert
    print(test)

    # assert test("zense")

    # element = self.driver.find_element(By.ID, "w3review")
    # print(element.get_attribute('value'))

    # ssn = self.driver.find_element(By.ID, "w3review")
    
    # if ssn.get_attribute('value') == None:
    #     ssn.send_keys("990-70-0007")
    # else:
    #     ssn.clear()
    #     ssn.send_keys("990-70-0007")
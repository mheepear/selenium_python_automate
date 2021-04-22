from selenium import webdriver
from faker import Faker
import random
from selenium.webdriver.common.keys import Keys



class ReusableModule(object):
    def provideDependent(self, args):
        randomNumber = random.randint(0, 6)
        driver = webdriver.Firefox()
        number = Faker.RandomInt
        elem = driver.find_element(By.Name, "kyc[dependents_number]").send_keys(randomNumber)
        if elem.randomNumber == 0:
        else elem.randomNumber > 1
# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestKycandy():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_kycandy(self):
    self.driver.get("http://portal.dev.getzense.com/")
    self.driver.set_window_size(1295, 735)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("andyfreddie@freddiemac.com")
    self.driver.find_element(By.ID, "loginForm").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Andy1234=")
    self.driver.find_element(By.CSS_SELECTOR, ".text-white").click()
    self.driver.find_element(By.LINK_TEXT, "Continue filling").click()
    self.driver.find_element(By.ID, "loan_purpose_purchase_button").click()
    self.driver.find_element(By.ID, "type_of_credit_joint_button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".overflow-hidden").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".overflow-hidden")
    dropdown.find_element(By.XPATH, "//option[. = '4']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .mb-4 > .appearance-none").click()
    self.driver.find_element(By.CSS_SELECTOR, ".border-trueblok-error").click()
    self.driver.find_element(By.CSS_SELECTOR, ".border-trueblok-error").send_keys("amyfreddie@freddiemac.com")
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) .appearance-none").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) .appearance-none").send_keys("alicefreddie@freddiemac.com")
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) .appearance-none").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) .appearance-none").send_keys("suzifreddie@freddiemac.com")
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > .mb-4 > .appearance-none").click()
    self.driver.find_element(By.CSS_SELECTOR, ".border-gray-700").send_keys("elizabethfreddie@freddiemac.com")
    self.driver.find_element(By.ID, "kyc_form").click()
    self.driver.find_element(By.ID, "continue_button").click()
    self.driver.find_element(By.NAME, "kyc[first_name]").click()
    self.driver.find_element(By.NAME, "kyc[first_name]").send_keys("Andy")
    self.driver.find_element(By.NAME, "kyc[last_name]").click()
    self.driver.find_element(By.NAME, "kyc[last_name]").send_keys("Freddie")
    self.driver.find_element(By.CSS_SELECTOR, ".leading-none").click()
    self.driver.find_element(By.NAME, "kyc[date_of_birth][0]").click()
    dropdown = self.driver.find_element(By.NAME, "kyc[date_of_birth][0]")
    dropdown.find_element(By.XPATH, "//option[. = 'MARCH']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".w-5\\/12 option:nth-child(4)").click()
    self.driver.find_element(By.NAME, "kyc[date_of_birth][1]").click()
    dropdown = self.driver.find_element(By.NAME, "kyc[date_of_birth][1]")
    dropdown.find_element(By.XPATH, "//option[. = '23']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".w-3\\/12 option:nth-child(24)").click()
    self.driver.find_element(By.NAME, "kyc[date_of_birth][2]").click()
    dropdown = self.driver.find_element(By.NAME, "kyc[date_of_birth][2]")
    dropdown.find_element(By.XPATH, "//option[. = '1971']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(43)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".leading-none").click()
    self.driver.find_element(By.NAME, "kyc[gender]").click()
    dropdown = self.driver.find_element(By.NAME, "kyc[gender]")
    dropdown.find_element(By.XPATH, "//option[. = 'MALE']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.NAME, "kyc[dependents_number]").click()
    dropdown = self.driver.find_element(By.NAME, "kyc[dependents_number]")
    dropdown.find_element(By.XPATH, "//option[. = '0']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.NAME, "kyc[citizenship]").click()
    dropdown = self.driver.find_element(By.NAME, "kyc[citizenship]")
    dropdown.find_element(By.XPATH, "//option[. = 'U.S. CITIZEN']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.NAME, "kyc[marital_status]").click()
    dropdown = self.driver.find_element(By.NAME, "kyc[marital_status]")
    dropdown.find_element(By.XPATH, "//option[. = 'MARRIED']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.ID, "ssn_number").click()
    self.driver.find_element(By.ID, "ssn_number").send_keys("xxx-xx-0003")
    self.driver.find_element(By.CSS_SELECTOR, ".fa-2x").click()
    self.driver.find_element(By.CSS_SELECTOR, ".leading-none").click()
    self.driver.find_element(By.NAME, "kyc[home_phone_number]").click()
    self.driver.find_element(By.NAME, "kyc[home_phone_number]").click()
    self.driver.find_element(By.NAME, "kyc[home_phone_number]").send_keys("(555) 222-2222")
    self.driver.find_element(By.NAME, "kyc[cell_phone_number]").click()
    self.driver.find_element(By.NAME, "kyc[cell_phone_number]").send_keys("(555) 333-3333")
    self.driver.find_element(By.NAME, "kyc[work_phone_number]").click()
    self.driver.find_element(By.NAME, "kyc[work_phone_number]").send_keys("(555) 999-9999")
    self.driver.find_element(By.CSS_SELECTOR, ".leading-none").click()
    self.driver.find_element(By.NAME, "current_address[street]").click()
    self.driver.find_element(By.NAME, "current_address[street]").click()
    self.driver.find_element(By.NAME, "current_address[street]").send_keys("4321")
    self.driver.find_element(By.NAME, "current_address[street]").click()
    self.driver.find_element(By.NAME, "current_address[street]").send_keys("4321 Cul de Sac St")
    self.driver.find_element(By.NAME, "current_address[city]").click()
    self.driver.find_element(By.NAME, "current_address[city]").send_keys("Someplace")
    self.driver.find_element(By.NAME, "current_address[zipcode]").click()
    self.driver.find_element(By.NAME, "current_address[zipcode]").send_keys("02723")
    self.driver.find_element(By.NAME, "current_address[years]").click()
    dropdown = self.driver.find_element(By.NAME, "current_address[years]")
    dropdown.find_element(By.XPATH, "//option[. = '2']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".pr-2 option:nth-child(4)").click()
    self.driver.find_element(By.NAME, "current_address[months]").click()
    dropdown = self.driver.find_element(By.NAME, "current_address[months]")
    dropdown.find_element(By.XPATH, "//option[. = '2']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".pl-2 option:nth-child(4)").click()
    self.driver.find_element(By.NAME, "current_address[housing]").click()
    dropdown = self.driver.find_element(By.NAME, "current_address[housing]")
    dropdown.find_element(By.XPATH, "//option[. = 'RENT']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".font-body > option:nth-child(4)").click()
    self.driver.find_element(By.NAME, "current_address[rent_per_month]").click()
    self.driver.find_element(By.NAME, "current_address[rent_per_month]").click()
    self.driver.find_element(By.NAME, "current_address[rent_per_month]").send_keys("$1,500")
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-checkbox").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.ID, "kyc_military_service_false").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.NAME, "kyc[language_preference]").click()
    dropdown = self.driver.find_element(By.NAME, "kyc[language_preference]")
    dropdown.find_element(By.XPATH, "//option[. = 'ENGLISH']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.ID, "knockout_question_9bd53ae6-99b3-45be-84e3-52b2cdd02849_false").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .flex-col > .w-full").click()
    self.driver.find_element(By.ID, "knockout_question_9388b75c-b3b6-442c-b955-aabf512902c3_false").click()
    self.driver.find_element(By.ID, "knockout_question_dafc6a06-83ca-45ff-bd1b-f1586db97cf7_false").click()
    self.driver.find_element(By.ID, "knockout_question_313120fb-0d79-4a9f-a029-19fce52b28b4_false").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.ID, "knockout_question_1b338701-2342-43d4-8efe-ee943e34c042_false").click()
    self.driver.find_element(By.ID, "knockout_question_e0776d4d-d0c5-49cc-896a-d70775c512ec_false").click()
    self.driver.find_element(By.ID, "knockout_question_48273e18-42b0-4ca9-9651-36f7a45ae77e_false").click()
    self.driver.find_element(By.ID, "knockout_question_1b5397ba-8223-4260-a483-c18d551415fc_false").click()
    self.driver.find_element(By.ID, "knockout_question_89bdb434-22b3-444e-b479-cb0330d3dfbf_false").click()
    self.driver.find_element(By.CSS_SELECTOR, ".leading-none").click()
    self.driver.find_element(By.NAME, "current_employments[0][employer_name]").click()
    self.driver.find_element(By.NAME, "current_employments[0][employer_name]").send_keys("Employer")
    self.driver.find_element(By.NAME, "current_employments[0][position]").click()
    self.driver.find_element(By.NAME, "current_employments[0][position]").send_keys("Employee")
    self.driver.find_element(By.NAME, "current_employments[0][phone]").click()
    self.driver.find_element(By.NAME, "current_employments[0][phone]").send_keys("(703) 555-1212")
    self.driver.find_element(By.NAME, "current_employments[0][street]").click()
    self.driver.find_element(By.NAME, "current_employments[0][street]").send_keys("Employer Address Rd")
    self.driver.find_element(By.NAME, "current_employments[0][city]").click()
    self.driver.find_element(By.NAME, "current_employments[0][city]").send_keys("Dawson")
    self.driver.find_element(By.NAME, "current_employments[0][state]").click()
    self.driver.find_element(By.NAME, "current_employments[0][state]").send_keys("IA")
    self.driver.find_element(By.NAME, "current_employments[0][zipcode]").click()
    self.driver.find_element(By.NAME, "current_employments[0][zipcode]").send_keys("50066")
    self.driver.find_element(By.NAME, "current_employments[0][start_date][0]").click()
    dropdown = self.driver.find_element(By.NAME, "current_employments[0][start_date][0]")
    dropdown.find_element(By.XPATH, "//option[. = 'JANUARY']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".w-5\\/12 option:nth-child(2)").click()
    self.driver.find_element(By.NAME, "current_employments[0][start_date][1]").click()
    dropdown = self.driver.find_element(By.NAME, "current_employments[0][start_date][1]")
    dropdown.find_element(By.XPATH, "//option[. = '1']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".w-3\\/12 option:nth-child(2)").click()
    self.driver.find_element(By.NAME, "current_employments[0][start_date][2]").click()
    dropdown = self.driver.find_element(By.NAME, "current_employments[0][start_date][2]")
    dropdown.find_element(By.XPATH, "//option[. = '2016']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(68)").click()
    self.driver.find_element(By.NAME, "current_employments[0][base_income]").click()
    self.driver.find_element(By.NAME, "current_employments[0][base_income]").send_keys("$7,680")
    self.driver.find_element(By.ID, "add_current_employment_income_0").click()
    element = self.driver.find_element(By.ID, "add_current_employment_income_0")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.ID, "add_another_job").click()
    self.driver.find_element(By.NAME, "assets[0][account_type]").click()
    self.driver.find_element(By.CSS_SELECTOR, "#kyc_form > div:nth-child(4)").click()
    self.driver.find_element(By.ID, "delete_asset_0").click()
    self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(3) > .flex:nth-child(1) > #add_another_job .w-5\\/6").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(3) > .flex:nth-child(1) > #add_another_job .w-5\\/6")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.NAME, "assets[0][account_type]").click()
    dropdown = self.driver.find_element(By.NAME, "assets[0][account_type]")
    dropdown.find_element(By.XPATH, "//option[. = 'OTHER']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(14)").click()
    self.driver.find_element(By.NAME, "assets[0][financial_institution]").click()
    self.driver.find_element(By.NAME, "assets[0][financial_institution]").send_keys("FinBank Profiles - A")
    self.driver.find_element(By.NAME, "assets[0][account_number]").click()
    self.driver.find_element(By.NAME, "assets[0][account_number]").send_keys("9223")
    self.driver.find_element(By.NAME, "assets[0][market_value]").click()
    self.driver.find_element(By.NAME, "assets[0][market_value]").send_keys("$45,000")
    self.driver.find_element(By.ID, "add_another_job").click()
    element = self.driver.find_element(By.ID, "add_another_job")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.NAME, "assets[1][account_type]").click()
    self.driver.find_element(By.NAME, "assets[1][account_type]").click()
    dropdown = self.driver.find_element(By.NAME, "assets[1][account_type]")
    dropdown.find_element(By.XPATH, "//option[. = 'SAVINGS']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-200:nth-child(4) option:nth-child(3)").click()
    self.driver.find_element(By.NAME, "assets[1][financial_institution]").click()
    self.driver.find_element(By.NAME, "assets[1][financial_institution]").send_keys("Dag Site")
    self.driver.find_element(By.NAME, "assets[1][account_number]").click()
    self.driver.find_element(By.NAME, "assets[1][account_number]").send_keys("109027")
    self.driver.find_element(By.NAME, "assets[1][market_value]").click()
    self.driver.find_element(By.NAME, "assets[1][market_value]").send_keys("$45,000")
    self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(2) > .flex:nth-child(1) > #add_another_job").click()
    self.driver.find_element(By.NAME, "liabilities[0][account_type]").click()
    dropdown = self.driver.find_element(By.NAME, "liabilities[0][account_type]")
    dropdown.find_element(By.XPATH, "//option[. = 'INSTALLMENT (e.g., car, student, personal loans)']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".inline-block:nth-child(2) > .overflow-hidden > option:nth-child(3)").click()
    self.driver.find_element(By.NAME, "liabilities[0][company_name]").click()
    self.driver.find_element(By.NAME, "liabilities[0][company_name]").click()
    self.driver.find_element(By.NAME, "liabilities[0][company_name]").send_keys("Relentless Bank")
    self.driver.find_element(By.NAME, "liabilities[0][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[0][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[0][account_number]").send_keys("87615524")
    self.driver.find_element(By.NAME, "liabilities[0][unpaid_balance]").click()
    self.driver.find_element(By.NAME, "liabilities[0][unpaid_balance]").send_keys("$1,554")
    self.driver.find_element(By.NAME, "liabilities[0][monthly_payment]").click()
    self.driver.find_element(By.NAME, "liabilities[0][monthly_payment]").send_keys("$46")
    self.driver.find_element(By.ID, "to_be_paid_off").click()
    dropdown = self.driver.find_element(By.ID, "to_be_paid_off")
    dropdown.find_element(By.XPATH, "//option[. = 'No']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#to_be_paid_off > option:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(3) > .flex:nth-child(1) > #add_another_job .w-5\\/6").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(3) > .flex:nth-child(1) > #add_another_job .w-5\\/6")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.NAME, "liabilities[1][account_type]").click()
    dropdown = self.driver.find_element(By.NAME, "liabilities[1][account_type]")
    dropdown.find_element(By.XPATH, "//option[. = 'REVOLVING (e.g., credit cards)']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-200:nth-child(3) > .flex > .w-full:nth-child(2) option:nth-child(2)").click()
    self.driver.find_element(By.NAME, "liabilities[1][company_name]").click()
    self.driver.find_element(By.NAME, "liabilities[1][company_name]").send_keys("Bursting Credit")
    self.driver.find_element(By.NAME, "liabilities[1][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[1][account_number]").send_keys("7612121")
    self.driver.find_element(By.NAME, "liabilities[1][unpaid_balance]").click()
    self.driver.find_element(By.NAME, "liabilities[1][unpaid_balance]").send_keys("$1,357")
    self.driver.find_element(By.NAME, "liabilities[1][monthly_payment]").click()
    self.driver.find_element(By.NAME, "liabilities[1][monthly_payment]").send_keys("$27")
    dropdown = self.driver.find_element(By.NAME, "liabilities[1][to_be_paid_off]")
    dropdown.find_element(By.XPATH, "//option[. = 'No']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-200:nth-child(3) #to_be_paid_off > option:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-200:nth-child(3) > .flex:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(4) > .flex:nth-child(1) > #add_another_job").click()
    element = self.driver.find_element(By.NAME, "liabilities[2][account_type]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "liabilities[2][account_type]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "liabilities[2][account_type]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.NAME, "liabilities[2][account_type]").click()
    dropdown = self.driver.find_element(By.NAME, "liabilities[2][account_type]")
    dropdown.find_element(By.XPATH, "//option[. = 'REVOLVING (e.g., credit cards)']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-200:nth-child(4) > .flex > .w-full:nth-child(2) option:nth-child(2)").click()
    self.driver.find_element(By.NAME, "liabilities[2][company_name]").click()
    self.driver.find_element(By.NAME, "liabilities[2][company_name]").click()
    self.driver.find_element(By.NAME, "liabilities[2][company_name]").send_keys("Prime Visa")
    self.driver.find_element(By.NAME, "liabilities[2][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[2][account_number]").send_keys("71542341")
    self.driver.find_element(By.NAME, "liabilities[2][unpaid_balance]").click()
    self.driver.find_element(By.NAME, "liabilities[2][unpaid_balance]").send_keys("$45")
    self.driver.find_element(By.NAME, "liabilities[2][monthly_payment]").click()
    self.driver.find_element(By.NAME, "liabilities[2][monthly_payment]").send_keys("$40")
    self.driver.find_element(By.NAME, "liabilities[2][to_be_paid_off]").click()
    dropdown = self.driver.find_element(By.NAME, "liabilities[2][to_be_paid_off]")
    dropdown.find_element(By.XPATH, "//option[. = 'No']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bg-gray-200:nth-child(4) #to_be_paid_off > option:nth-child(3)").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.ID, "kyc_real_estate_false").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.ID, "kyc_back_button").click()
    self.driver.find_element(By.ID, "kyc_back_button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(1) > .w-full > .flex .flex:nth-child(3) > #add_another_job").click()
    self.driver.find_element(By.NAME, "other_assets[0][asset_type]").click()
    self.driver.find_element(By.NAME, "other_assets[0][asset_type]").click()
    dropdown = self.driver.find_element(By.NAME, "other_assets[0][asset_type]")
    dropdown.find_element(By.XPATH, "//option[. = 'OTHER']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".inline-block:nth-child(2) option:nth-child(10)").click()
    self.driver.find_element(By.NAME, "other_assets[0][market_value]").click()
    self.driver.find_element(By.NAME, "other_assets[0][market_value]").click()
    self.driver.find_element(By.NAME, "other_assets[0][market_value]").send_keys("$100")
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.ID, "kyc_real_estate_false").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.ID, "kyc_back_button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".inline-block").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.ID, "kyc_real_estate_false").click()
    self.driver.find_element(By.CSS_SELECTOR, ".leading-none").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.ID, "questionnaire_a_occupy_as_primary_residence_yes").click()
    self.driver.find_element(By.ID, "questionnaire_b_ownership_interest_no").click()
    self.driver.find_element(By.ID, "questionnaire_b_family_relationship_no").click()
    self.driver.find_element(By.ID, "questionnaire_c_borrowing_money_no").click()
    self.driver.find_element(By.ID, "questionnaire_d_apply_for_mortgage_no").click()
    self.driver.find_element(By.ID, "questionnaire_d_apply_for_new_credit_no").click()
    self.driver.find_element(By.ID, "questionnaire_e_subject_to_lien_no").click()
    self.driver.find_element(By.CSS_SELECTOR, ".leading-none").click()
    self.driver.find_element(By.ID, "questionnaire_a2_co_signer_no").click()
    self.driver.find_element(By.ID, "questionnaire_b2_outstanding_judgement_no").click()
    self.driver.find_element(By.ID, "questionnaire_c2_delinquent_no").click()
    self.driver.find_element(By.ID, "questionnaire_d2_lawsuit_no").click()
    self.driver.find_element(By.ID, "questionnaire_e2_conveyed_title_to_property_no").click()
    self.driver.find_element(By.ID, "questionnaire_f2_pre_foreclosure_sale_no").click()
    self.driver.find_element(By.ID, "questionnaire_g2_property_foreclosed_no").click()
    self.driver.find_element(By.ID, "questionnaire_h2_bankruptcy_no").click()
    self.driver.find_element(By.CSS_SELECTOR, ".leading-none").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .pt-6:nth-child(3) > .trueblok-radio").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .pt-6:nth-child(4) .trueblok-checkmark").click()
    self.driver.find_element(By.CSS_SELECTOR, ".pt-6:nth-child(6) .trueblok-checkmark").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
    self.driver.find_element(By.NAME, "property_address[street]").click()
    self.driver.find_element(By.NAME, "property_address[street]").send_keys("2422 Knapps way")
    self.driver.find_element(By.NAME, "property_address[unit]").click()
    self.driver.find_element(By.NAME, "property_address[state]").click()
    self.driver.find_element(By.NAME, "property_address[state]").send_keys("MD")
    self.driver.find_element(By.NAME, "property_address[city]").click()
    self.driver.find_element(By.NAME, "property_address[city]").send_keys("Odenton")
    self.driver.find_element(By.NAME, "property_address[zipcode]").click()
    self.driver.find_element(By.NAME, "property_address[zipcode]").send_keys("21113")
    self.driver.find_element(By.NAME, "property_address[occupancy]").click()
    dropdown = self.driver.find_element(By.NAME, "property_address[occupancy]")
    dropdown.find_element(By.XPATH, "//option[. = 'PRIMARY RESIDENCE']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(8) option:nth-child(2)").click()
    self.driver.find_element(By.NAME, "property_address[property_type]").click()
    self.driver.find_element(By.NAME, "property_address[property_type]").click()
    dropdown = self.driver.find_element(By.NAME, "property_address[property_type]")
    dropdown.find_element(By.XPATH, "//option[. = 'SINGLE FAMILY RESIDENTIAL']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(9) option:nth-child(2)").click()
    self.driver.find_element(By.NAME, "property_address[loan_amount]").click()
    self.driver.find_element(By.NAME, "property_address[loan_amount]").click()
    self.driver.find_element(By.NAME, "property_address[loan_amount]").send_keys("$210,000")
    self.driver.find_element(By.CSS_SELECTOR, ".leading-none").click()
    self.driver.find_element(By.CSS_SELECTOR, "#package_0_li3 > .w-1\\/2:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bg-trueblok-primary:nth-child(2)").click()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, ".cb_label").click()
    self.driver.find_element(By.ID, "action-bar-btn-continue").click()
    element = self.driver.find_element(By.ID, "action-bar-btn-continue")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#navigate-btn > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".tab-image").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".item-alt-inline-block:nth-child(1)").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "action-bar-btn-finish").click()
    self.driver.find_element(By.LINK_TEXT, "GO BACK TO DASHBOARD").click()
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, ".w-3\\/5").click()
  

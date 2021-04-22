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
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

class TestKycandy():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  # def teardown_method(self, method):
  #   self.driver.quit()
  
  def test_kycandy(self):
    self.driver.get("http://portal.dev.getzense.com/")
    # wait for element and click #
    loginbutton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.LINK_TEXT, "Log in")))
    loginbutton.click()
    ##############################

    # Authentication
    elementlogin = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "email")))
    elementlogin.click()
    self.driver.find_element(By.ID, "email").send_keys("andydv06test2@mail.com") # maindv01@mail.com
    self.driver.find_element(By.ID, "password").send_keys("Main1234=")  # Main1234=
    self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[1]/form/div[3]/div[3]/button").click()
######################################

    # Start KYC
    kyctrigger = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div[2]/a")))
    kyctrigger.click()
######################################

    # # Step 00 Loan Purpose
    # loanpurpose = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "loan_purpose_purchase_button"))) #loan_purpose_purchase_button
    # loanpurpose.click()
    # loanjoint = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "type_of_credit_joint_button")))
    # loanjoint.click()    
    # Select(self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[2]/select")).select_by_value('1')
    # self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[3]/div/div/input[2]").send_keys("amydv06test1@mail.com") #Cotest1234=
    # self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[4]/button").click()

#####################################

#     # Step 01 Full name
#     name = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[first_name]")))
#     name.clear()
#     name.send_keys("Andy")
#     lname = self.driver.find_element(By.NAME, "kyc[last_name]")
#     lname.clear()
#     lname = self.driver.find_element(By.NAME, "kyc[last_name]").send_keys("Freddie")
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 02 Birth Date
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][0]")).select_by_value('MARCH')
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][1]")).select_by_value('23')
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][2]")).select_by_value('1971')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 03 Gender
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     Select(self.driver.find_element(By.NAME, "kyc[gender]")).select_by_value('MALE')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 04 Dependents
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[dependents_number]")))
#     Select(self.driver.find_element(By.NAME, "kyc[dependents_number]")).select_by_value('2')
#     WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((By.NAME, "kyc[dependents_ages][0]")))
#     self.driver.find_element(By.NAME, "kyc[dependents_ages][0]").clear()
#     self.driver.find_element(By.NAME, "kyc[dependents_ages][0]").send_keys("15")
#     self.driver.find_element(By.NAME, "kyc[dependents_ages][1]").clear()
#     self.driver.find_element(By.NAME, "kyc[dependents_ages][1]").send_keys("17")

#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 05 Citizenship
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[citizenship]")))
#     Select(self.driver.find_element(By.NAME, "kyc[citizenship]")).select_by_value('U.S. CITIZEN')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
#     #####################################

#     # Step 06 Marital Status
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[marital_status]")))
#     Select(self.driver.find_element(By.NAME, "kyc[marital_status]")).select_by_value('MARRIED')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 07 SSN
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "ssn_number")))

#     ssn = self.driver.find_element(By.ID, "ssn_number")
#     if ssn.get_attribute('Value') == None:
#         ssn.send_keys("990-30-0003")
#     else:
#         ssn.clear()
#         ssn.send_keys("990-30-0003")

#     self.driver.find_element(By.CSS_SELECTOR, ".fa-2x").click()
#     self.driver.find_element(By.ID, "kyc_step7_next_button").click()
# #####################################

#     # Step 08 Phone Number
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[home_phone_number]")))
#     self.driver.find_element(By.NAME, "kyc[home_phone_number]").clear()
#     self.driver.find_element(By.NAME, "kyc[home_phone_number]").send_keys("(555) 333-4444" ) #Home 
#     self.driver.find_element(By.NAME, "kyc[cell_phone_number]").clear()
#     self.driver.find_element(By.NAME, "kyc[cell_phone_number]").send_keys("(555) 555-6666") #Cell
#     self.driver.find_element(By.NAME, "kyc[work_phone_number]").clear()
#     self.driver.find_element(By.NAME, "kyc[work_phone_number]").send_keys("(555) 777-8888") #Work
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 09 Current Address
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "current_address[street]")))
#     # self.driver.find_element(By.NAME, "current_address[street]").click()
#     self.driver.find_element(By.NAME, "current_address[street]").clear()
#     self.driver.find_element(By.NAME, "current_address[street]").send_keys("4321 Cul de Sac Street")
#     # self.driver.find_element(By.NAME, "current_address[city]").click()
#     self.driver.find_element(By.NAME, "current_address[city]").send_keys("Someplace")
#     self.driver.find_element(By.NAME, "current_address[city]").clear()
#     # self.driver.find_element(By.NAME, "current_address[zipcode]").click()
#     self.driver.find_element(By.NAME, "current_address[zipcode]").send_keys("02723")
#     self.driver.find_element(By.NAME, "current_address[zipcode]").clear()
#     # self.driver.find_element(By.NAME, "current_address[years]").click()
#     Select(self.driver.find_element(By.NAME, "current_address[years]")).select_by_value('2')
#     Select(self.driver.find_element(By.NAME, "current_address[months]")).select_by_value('2')
#     Select(self.driver.find_element(By.NAME, "current_address[housing]")).select_by_value('RENT')
#     # self.driver.find_element(By.NAME, "current_address[rent_per_month]").click()
#     self.driver.find_element(By.NAME, "current_address[rent_per_month]").clear()
#     self.driver.find_element(By.NAME, "current_address[rent_per_month]").send_keys("1500")
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# ####################################

#     # Step 10 Mailing Address
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label/input[2]")))

#     check = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label/input[2]")    
#     check.click()
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################
   
#     # Step 11 served army
#     military = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_military_service_true")))
#     military.click()

#     self.driver.find_element(By.CSS_SELECTOR, "div.shadow:nth-child(2) > fieldset:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(3)").click()

#     Select(self.driver.find_element(By.NAME, "kyc[military_currently_serving_expiration_year]")).select_by_value('9')
#     Select(self.driver.find_element(By.NAME, "kyc[military_currently_serving_expiration_month]")).select_by_value('0')
#     self.driver.find_element(By.NAME, "militaryIncome[military_division]").send_keys("US Army")
#     Select(self.driver.find_element(By.NAME, "militaryIncome[start_date][0]")).select_by_value('JANUARY')
#     Select(self.driver.find_element(By.NAME, "militaryIncome[start_date][1]")).select_by_value('1')
#     Select(self.driver.find_element(By.NAME, "militaryIncome[start_date][2]")).select_by_value('2000')

#     self.driver.find_element(By.ID, "add_military_income").click()
#     self.driver.find_element(By.NAME, "militaryIncome[base_income]").send_keys("7580")
#     self.driver.find_element(By.NAME, "militaryIncome[prop_income]").send_keys("250")
#     self.driver.find_element(By.NAME, "militaryIncome[quarters_allowance]").send_keys("550")

#     nextbtn = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))

#     nextbtn.click()
# #####################################

#     # Step 12 preferred language
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[language_preference]")))
#     Select(self.driver.find_element(By.NAME, "kyc[language_preference]")).select_by_value('ENGLISH')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 13 Please tell us about your income.
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     self.driver.find_element(By.ID, "knockout_question_9bd53ae6-99b3-45be-84e3-52b2cdd02849_true").click()
#     self.driver.find_element(By.ID, "knockout_question_9388b75c-b3b6-442c-b955-aabf512902c3_false").click()
#     self.driver.find_element(By.ID, "knockout_question_dafc6a06-83ca-45ff-bd1b-f1586db97cf7_false").click()
#     self.driver.find_element(By.ID, "knockout_question_313120fb-0d79-4a9f-a029-19fce52b28b4_false").click()
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 14 Please tell us about your credit.
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     self.driver.find_element(By.ID, "knockout_question_1b338701-2342-43d4-8efe-ee943e34c042_false").click()
#     self.driver.find_element(By.ID, "knockout_question_e0776d4d-d0c5-49cc-896a-d70775c512ec_false").click()
#     self.driver.find_element(By.ID, "knockout_question_48273e18-42b0-4ca9-9651-36f7a45ae77e_false").click()
#     self.driver.find_element(By.ID, "knockout_question_1b5397ba-8223-4260-a483-c18d551415fc_false").click()
#     self.driver.find_element(By.ID, "knockout_question_89bdb434-22b3-444e-b479-cb0330d3dfbf_false").click()
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 15 Tell us about your employment.
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))

#     self.driver.find_element(By.NAME, "current_employments[0][employer_name]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][employer_name]").send_keys("US Army")
#     self.driver.find_element(By.NAME, "current_employments[0][position]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][position]").send_keys("Major")
#     self.driver.find_element(By.NAME, "current_employments[0][phone]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][phone]").send_keys("6667778888")
#     self.driver.find_element(By.NAME, "current_employments[0][street]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][street]").send_keys("2400 US Army Dr.")
#     self.driver.find_element(By.NAME, "current_employments[0][city]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][city]").send_keys("Someplace")
#     self.driver.find_element(By.NAME, "current_employments[0][state]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][state]").send_keys("MA")
#     self.driver.find_element(By.NAME, "current_employments[0][zipcode]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][zipcode]").send_keys("02723")
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][0]")).select_by_value('JANUARY')
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][1]")).select_by_value('1')
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][2]")).select_by_value('2000')
#     # self.driver.find_element(By.NAME, "current_employments[0][base_income]").click()

#     self.driver.find_element(By.ID, "add_current_employment_income_0").click()
#     self.driver.find_element(By.NAME, "current_employments[0][base_income]").send_keys("7580")
#     self.driver.find_element(By.NAME, "current_employments[0][military_entitlements]").send_keys("800")


#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

    # Step 16 Tell us about your assets.
        ####### 1st asset #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    
    Select(self.driver.find_element(By.NAME, "assets[0][account_type]")).select_by_value('SAVINGS') 
    # self.driver.find_element(By.NAME, "assets[0][financial_institution]").click()
    self.driver.find_element(By.NAME, "assets[0][financial_institution]").send_keys("FinBank Profiles - A")
    # self.driver.find_element(By.NAME, "assets[0][account_number]").click()
    self.driver.find_element(By.NAME, "assets[0][account_number]").send_keys("9018")
    # self.driver.find_element(By.NAME, "assets[0][market_value]").click()
    self.driver.find_element(By.NAME, "assets[0][market_value]").send_keys("20000")

        ####### 2nd asset #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[1][account_type]")).select_by_value('CHECKING') 
    self.driver.find_element(By.NAME, "assets[1][financial_institution]").send_keys("Dag Site")
    # self.driver.find_element(By.NAME, "assets[1][account_number]").click()
    self.driver.find_element(By.NAME, "assets[1][account_number]").send_keys("109023")
    # self.driver.find_element(By.NAME, "assets[1][market_value]").click()
    self.driver.find_element(By.NAME, "assets[1][market_value]").send_keys("36000")

        ####### 3rd asset #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[2][account_type]")).select_by_value('MONEY MARKET FUND') 
    self.driver.find_element(By.NAME, "assets[2][financial_institution]").send_keys("PenFed")
    # self.driver.find_element(By.NAME, "assets[2][account_number]").click()
    self.driver.find_element(By.NAME, "assets[2][account_number]").send_keys("852147")
    # self.driver.find_element(By.NAME, "assets[2][market_value]").click()
    self.driver.find_element(By.NAME, "assets[2][market_value]").send_keys("110000")

        ###### 1st liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[0][account_type]")).select_by_value('INSTALLMENT (e.g., car, student, personal loans)') 
    self.driver.find_element(By.NAME, "liabilities[0][company_name]").send_keys("Relentless Bank")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[0][account_number]").send_keys("87615524")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[0][unpaid_balance]").send_keys("1554")
    self.driver.find_element(By.NAME, "liabilities[0][monthly_payment]").send_keys("46")
    Select(self.driver.find_element(By.NAME, "liabilities[0][to_be_paid_off]")).select_by_value('false')

        ###### 2nd liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[1][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[1][company_name]").send_keys("Bursting Credit")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[1][account_number]").send_keys("7612121")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[1][unpaid_balance]").send_keys("1357")
    self.driver.find_element(By.NAME, "liabilities[1][monthly_payment]").send_keys("27")
    Select(self.driver.find_element(By.NAME, "liabilities[1][to_be_paid_off]")).select_by_value('false')

        ###### 3rd liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[2][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[2][company_name]").send_keys("Prime Visa")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[2][account_number]").send_keys("71542341")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[2][unpaid_balance]").send_keys("45")
    self.driver.find_element(By.NAME, "liabilities[2][monthly_payment]").send_keys("40")
    Select(self.driver.find_element(By.NAME, "liabilities[2][to_be_paid_off]")).select_by_value('false')

        ###### 4th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[3][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[3][company_name]").send_keys("Capital Bank")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[3][account_number]").send_keys("85746187")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[3][unpaid_balance]").send_keys("29")
    self.driver.find_element(By.NAME, "liabilities[3][monthly_payment]").send_keys("10")
    Select(self.driver.find_element(By.NAME, "liabilities[3][to_be_paid_off]")).select_by_value('false')

        ###### 5th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[4][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[4][company_name]").send_keys("Allen Bank Card")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[4][account_number]").send_keys("761546413")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[4][unpaid_balance]").send_keys("4665")
    self.driver.find_element(By.NAME, "liabilities[4][monthly_payment]").send_keys("133")
    Select(self.driver.find_element(By.NAME, "liabilities[4][to_be_paid_off]")).select_by_value('true')

    self.driver.find_element(By.ID, "kyc_next_button").click()
####################################


    # Step 17 Tell us about your property.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_real_estate_false")))
    self.driver.find_element(By.ID, "kyc_real_estate_false").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()

####################################

    # Step 19 Let's find out more about your mortgage.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))

    self.driver.find_element(By.ID, "kyc_next_button").click()

#####################################

    # Step 20 Provide us with your property information.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.ID, "questionnaire_a_occupy_as_primary_residence_yes").click()
    self.driver.find_element(By.ID, "questionnaire_b_ownership_interest_no").click()
    self.driver.find_element(By.ID, "questionnaire_b_family_relationship_no").click()
    self.driver.find_element(By.ID, "questionnaire_c_borrowing_money_no").click()
    self.driver.find_element(By.ID, "questionnaire_d_apply_for_mortgage_no").click()
    self.driver.find_element(By.ID, "questionnaire_d_apply_for_new_credit_no").click()
    self.driver.find_element(By.ID, "questionnaire_e_subject_to_lien_no").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 21 Provide us with your finance detail.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.ID, "questionnaire_a2_co_signer_no").click()
    self.driver.find_element(By.ID, "questionnaire_b2_outstanding_judgement_no").click()
    self.driver.find_element(By.ID, "questionnaire_c2_delinquent_no").click()
    self.driver.find_element(By.ID, "questionnaire_d2_lawsuit_no").click()
    self.driver.find_element(By.ID, "questionnaire_e2_conveyed_title_to_property_no").click()
    self.driver.find_element(By.ID, "questionnaire_f2_pre_foreclosure_sale_no").click()
    self.driver.find_element(By.ID, "questionnaire_g2_property_foreclosed_no").click()
    self.driver.find_element(By.ID, "questionnaire_h2_bankruptcy_no").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 22 Can you tell us about your race and ethnicity.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.CSS_SELECTOR, ".m-2 > div:nth-child(2) > div:nth-child(3) > label:nth-child(1) > input:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "div.pt-6:nth-child(6) > label:nth-child(1) > input:nth-child(1)").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 23 Purchase
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.NAME, "property_address[street]").send_keys("2442 Knapps Way")
    self.driver.find_element(By.NAME, "property_address[state]").send_keys("MD")
    self.driver.find_element(By.NAME, "property_address[city]").send_keys("Odenton")
    self.driver.find_element(By.NAME, "property_address[zipcode]").send_keys("21113")
    Select(self.driver.find_element(By.NAME, "property_address[occupancy]")).select_by_value('PR')
    Select(self.driver.find_element(By.NAME, "property_address[property_type]")).select_by_value('SFR')


    self.driver.find_element(By.ID, "property_in_project_false").click()
    self.driver.find_element(By.ID, "mix_usage_false").click()
    self.driver.find_element(By.ID, "clean_energy_lien_false").click()

    # expense
    self.driver.find_element(By.ID, "add_expense").click()
    Select(self.driver.find_element(By.NAME, "expenses[0][type]")).select_by_value('FIRST MORTGAGE PRINCIPAL AND INTEREST')
    self.driver.find_element(By.NAME, "expenses[0][amount]").send_keys("1553.35")

    self.driver.find_element(By.ID, "add_expense").click()
    Select(self.driver.find_element(By.NAME, "expenses[1][type]")).select_by_value('HOME OWNERS INSURANCE')
    self.driver.find_element(By.NAME, "expenses[1][amount]").send_keys("75")

    self.driver.find_element(By.ID, "add_expense").click()
    Select(self.driver.find_element(By.NAME, "expenses[2][type]")).select_by_value('REAL ESTATE TAX')
    self.driver.find_element(By.NAME, "expenses[2][amount]").send_keys("250")


    self.driver.find_element(By.NAME, "property_address[loan_amount]").send_keys("275000")
    self.driver.find_element(By.ID, "kyc_next_button").click()

#####################################

    # # Step 24 Docusign
    # WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#package_0_inner_div")))
    # self.driver.find_element(By.CSS_SELECTOR, "#package_0_inner_div").click()

    # self.driver.find_element(By.NAME, "action").click()
    # self.driver.switch_to.frame(0)
    # self.driver.find_element(By.CSS_SELECTOR, ".cb_label").click()
    # self.driver.find_element(By.ID, "action-bar-btn-continue").click()
    # element = self.driver.find_element(By.ID, "action-bar-btn-continue")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element).perform()
    # element = self.driver.find_element(By.CSS_SELECTOR, "body")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element, 0, 0).perform()
    # self.driver.find_element(By.CSS_SELECTOR, "#navigate-btn > span").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".tab-image").click()
    # self.driver.execute_script("window.scrollTo(0,0)")
    # self.driver.find_element(By.CSS_SELECTOR, ".item-alt-inline-block:nth-child(1)").click()
    # self.driver.execute_script("window.scrollTo(0,0)")
    # self.driver.find_element(By.ID, "action-bar-btn-finish").click()
    # self.driver.find_element(By.LINK_TEXT, "GO BACK TO DASHBOARD").click()
    # self.driver.switch_to.default_content()
    # self.driver.find_element(By.CSS_SELECTOR, ".w-3\\/5").click()
  

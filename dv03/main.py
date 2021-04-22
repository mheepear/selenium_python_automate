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
    self.driver.find_element(By.ID, "email").send_keys("suzidv03test1@mail.com") # maindv01@mail.com
    self.driver.find_element(By.ID, "password").send_keys("Main1234=")  # Main1234=
    self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[1]/form/div[3]/div[3]/button").click()
######################################

    # Start KYC
    kyctrigger = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div[2]/a")))
    kyctrigger.click()
######################################

#     # Step 00 Loan Purpose
#     loanpurpose = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "loan_purpose_refinance_button"))) #loan_purpose_purchase_button
#     loanpurpose.click()
#     loan = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "type_of_credit_individual_button")))
#     loan.click()    
#     self.driver.find_element(By.ID, "continue_button").click()

# ######################################

#     # Step 01 Full name
#     self.driver.implicitly_wait(5) # seconds
#     name = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[first_name]")))
#     name.send_keys("Suzi")
#     self.driver.find_element(By.NAME, "kyc[last_name]").send_keys("Freddie03")
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 02 Birth Date
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][0]")).select_by_value('JULY')
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][1]")).select_by_value('9')
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][2]")).select_by_value('1974')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 03 Gender
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     Select(self.driver.find_element(By.NAME, "kyc[gender]")).select_by_value('FEMALE')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 04 Dependents
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[dependents_number]")))
#     Select(self.driver.find_element(By.NAME, "kyc[dependents_number]")).select_by_value('0')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 05 Citizenship
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[citizenship]")))
#     Select(self.driver.find_element(By.NAME, "kyc[citizenship]")).select_by_value('U.S. CITIZEN')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 06 Marital Status
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[marital_status]")))
#     Select(self.driver.find_element(By.NAME, "kyc[marital_status]")).select_by_value('UNMARRIED')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 07 SSN
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "ssn_number")))
#     # ssn = self.driver.find_element(By.ID, "ssn_number")
#     # if ssn == null:
#     #     ssn.send_keys("990-70-0007")
#     # else:
#     #     ssn.clear_field()
#     self.driver.find_element(By.ID, "ssn_number").send_keys("990-70-0007")
#     self.driver.find_element(By.CSS_SELECTOR, ".fa-2x").click()
#     self.driver.find_element(By.ID, "kyc_step7_next_button").click()
# #####################################

    # Step 08 Phone Number
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[home_phone_number]")))
    # self.driver.find_element(By.NAME, "kyc[home_phone_number]").click()
    self.driver.find_element(By.NAME, "kyc[home_phone_number]").send_keys("(777) 777-7777" ) #Home 
    # self.driver.find_element(By.NAME, "kyc[cell_phone_number]").click()
    self.driver.find_element(By.NAME, "kyc[cell_phone_number]").send_keys("(888) 888-8888") #Cell
    # self.driver.find_element(By.NAME, "kyc[work_phone_number]").click()
    self.driver.find_element(By.NAME, "kyc[work_phone_number]").send_keys("(999) 999-9999") #Work
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 09 Current Address
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "current_address[street]")))
    # self.driver.find_element(By.NAME, "current_address[street]").click()
    self.driver.find_element(By.NAME, "current_address[street]").send_keys("5404 Pawnee Trail")
    # self.driver.find_element(By.NAME, "current_address[city]").click()
    self.driver.find_element(By.NAME, "current_address[city]").send_keys("Louisville")
    # self.driver.find_element(By.NAME, "current_address[zipcode]").click()
    self.driver.find_element(By.NAME, "current_address[zipcode]").send_keys("40207")
    # self.driver.find_element(By.NAME, "current_address[years]").click()
    Select(self.driver.find_element(By.NAME, "current_address[years]")).select_by_value('2')
    Select(self.driver.find_element(By.NAME, "current_address[months]")).select_by_value('6')
    Select(self.driver.find_element(By.NAME, "current_address[housing]")).select_by_value('RENT')
    # self.driver.find_element(By.NAME, "current_address[rent_per_month]").click()
    self.driver.find_element(By.NAME, "current_address[rent_per_month]").send_keys("1500")
    self.driver.find_element(By.ID, "kyc_next_button").click()
####################################

    # Step 10 Mailing Address
    check = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label/input[2]")))
    check.click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################
   
    # Step 11 served army
    military = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_military_service_false")))
    military.click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 12 preferred language
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[language_preference]")))
    Select(self.driver.find_element(By.NAME, "kyc[language_preference]")).select_by_value('ENGLISH')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 13 Please tell us about your income.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.ID, "knockout_question_9bd53ae6-99b3-45be-84e3-52b2cdd02849_true").click()
    self.driver.find_element(By.ID, "knockout_question_9388b75c-b3b6-442c-b955-aabf512902c3_false").click()
    self.driver.find_element(By.ID, "knockout_question_dafc6a06-83ca-45ff-bd1b-f1586db97cf7_false").click()
    self.driver.find_element(By.ID, "knockout_question_313120fb-0d79-4a9f-a029-19fce52b28b4_false").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 14 Please tell us about your credit.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.ID, "knockout_question_1b338701-2342-43d4-8efe-ee943e34c042_false").click()
    self.driver.find_element(By.ID, "knockout_question_e0776d4d-d0c5-49cc-896a-d70775c512ec_false").click()
    self.driver.find_element(By.ID, "knockout_question_48273e18-42b0-4ca9-9651-36f7a45ae77e_false").click()
    self.driver.find_element(By.ID, "knockout_question_1b5397ba-8223-4260-a483-c18d551415fc_false").click()
    self.driver.find_element(By.ID, "knockout_question_89bdb434-22b3-444e-b479-cb0330d3dfbf_false").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 15 Tell us about your employment.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.NAME, "current_employments[0][employer_name]").send_keys("Cardinal Homes")
    # self.driver.find_element(By.NAME, "current_employments[0][position]").click()
    self.driver.find_element(By.NAME, "current_employments[0][position]").send_keys("Sole Owner")
    # self.driver.find_element(By.NAME, "current_employments[0][phone]").click()
    self.driver.find_element(By.NAME, "current_employments[0][phone]").send_keys("7777777777")
    # self.driver.find_element(By.NAME, "current_employments[0][street]").click()
    self.driver.find_element(By.NAME, "current_employments[0][street]").send_keys("5404 Pawnee Trail")
    # self.driver.find_element(By.NAME, "current_employments[0][city]").click()
    self.driver.find_element(By.NAME, "current_employments[0][city]").send_keys("Lousiville")
    # self.driver.find_element(By.NAME, "current_employments[0][state]").click()
    self.driver.find_element(By.NAME, "current_employments[0][state]").send_keys("KY")
    # self.driver.find_element(By.NAME, "current_employments[0][zipcode]").click()
    self.driver.find_element(By.NAME, "current_employments[0][zipcode]").send_keys("40207")
    # self.driver.find_element(By.NAME, "current_employments[0][start_date][0]").click()
    Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][0]")).select_by_value('JULY')
    Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][1]")).select_by_value('24')
    Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][2]")).select_by_value('1999')
    # self.driver.find_element(By.NAME, "current_employments[0][base_income]").click()

    self.driver.find_element(By.NAME, "current_employments[0][base_income]").send_keys("19500")
    self.driver.find_element(By.CSS_SELECTOR, "div.flex:nth-child(8) > div:nth-child(1) > label:nth-child(1) > div:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "label.trueblok-radio:nth-child(2) > span:nth-child(2)").click()
    self.driver.find_element(By.NAME, "current_employments[0][business_owner_monthly_income]").send_keys("19500")
    # self.driver.find_element(By.NAME, "current_employments[0][base_income]").click()

    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 16 Tell us about your assets.
        ####### 1st asset #######
    WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()

    Select(self.driver.find_element(By.NAME, "assets[0][account_type]")).select_by_value('CHECKING') 
    # self.driver.find_element(By.NAME, "assets[0][financial_institution]").click()
    self.driver.find_element(By.NAME, "assets[0][financial_institution]").send_keys("FinBank Profiles - A")
    # self.driver.find_element(By.NAME, "assets[0][account_number]").click()
    self.driver.find_element(By.NAME, "assets[0][account_number]").send_keys("9889")
    # self.driver.find_element(By.NAME, "assets[0][market_value]").click()
    self.driver.find_element(By.NAME, "assets[0][market_value]").send_keys("45000")

        ####### 2nd asset #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[1][account_type]")).select_by_value('SAVINGS') 
    self.driver.find_element(By.NAME, "assets[1][financial_institution]").send_keys("The Bank")
    # self.driver.find_element(By.NAME, "assets[1][account_number]").click()
    self.driver.find_element(By.NAME, "assets[1][account_number]").send_keys("345234234")
    # self.driver.find_element(By.NAME, "assets[1][market_value]").click()
    self.driver.find_element(By.NAME, "assets[1][market_value]").send_keys("128900")

        ###### 1st liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[0][account_type]")).select_by_value('MORTGAGE LOAN') 
    self.driver.find_element(By.NAME, "liabilities[0][company_name]").send_keys("KENTUCKY NATIONAL")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[0][account_number]").send_keys("1234567")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[0][unpaid_balance]").send_keys("123773")
    self.driver.find_element(By.NAME, "liabilities[0][monthly_payment]").send_keys("817")
    Select(self.driver.find_element(By.NAME, "liabilities[0][to_be_paid_off]")).select_by_value('true')

        ###### 2nd liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[1][account_type]")).select_by_value('INSTALLMENT (e.g., car, student, personal loans)') 
    self.driver.find_element(By.NAME, "liabilities[1][company_name]").send_keys("Bank One")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[1][account_number]").send_keys("0756")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[1][unpaid_balance]").send_keys("5342")
    self.driver.find_element(By.NAME, "liabilities[1][monthly_payment]").send_keys("217")
    Select(self.driver.find_element(By.NAME, "liabilities[1][to_be_paid_off]")).select_by_value('false')

        ###### 3rd liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[2][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[2][company_name]").send_keys("Hobbs Bank")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[2][account_number]").send_keys("1300")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[2][unpaid_balance]").send_keys("3673")
    self.driver.find_element(By.NAME, "liabilities[2][monthly_payment]").send_keys("80")
    Select(self.driver.find_element(By.NAME, "liabilities[2][to_be_paid_off]")).select_by_value('false')

        ###### 4th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[3][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[3][company_name]").send_keys("ATT Universal")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[3][account_number]").send_keys("1440")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[3][unpaid_balance]").send_keys("3350")
    self.driver.find_element(By.NAME, "liabilities[3][monthly_payment]").send_keys("67")
    Select(self.driver.find_element(By.NAME, "liabilities[3][to_be_paid_off]")).select_by_value('false')

            ###### 5th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[4][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[4][company_name]").send_keys("GE Card")
    # self.driver.find_element(By.NAME, "assets[4][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[4][account_number]").send_keys("0756")
    # self.driver.find_element(By.NAME, "assets[4][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[4][unpaid_balance]").send_keys("3114")
    self.driver.find_element(By.NAME, "liabilities[4][monthly_payment]").send_keys("63")
    Select(self.driver.find_element(By.NAME, "liabilities[4][to_be_paid_off]")).select_by_value('false')

        ###### 6th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[5][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[5][company_name]").send_keys("First USA")
    # self.driver.find_element(By.NAME, "assets[5][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[5][account_number]").send_keys("1716")
    # self.driver.find_element(By.NAME, "assets[5][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[5][unpaid_balance]").send_keys("2050")
    self.driver.find_element(By.NAME, "liabilities[5][monthly_payment]").send_keys("41")
    Select(self.driver.find_element(By.NAME, "liabilities[5][to_be_paid_off]")).select_by_value('false')

        ###### 7th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[6][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[6][company_name]").send_keys("Discover")
    # self.driver.find_element(By.NAME, "assets[6][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[6][account_number]").send_keys("1100")
    # self.driver.find_element(By.NAME, "assets[6][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[6][unpaid_balance]").send_keys("1800")
    self.driver.find_element(By.NAME, "liabilities[6][monthly_payment]").send_keys("36")
    Select(self.driver.find_element(By.NAME, "liabilities[6][to_be_paid_off]")).select_by_value('false')

        ###### 7th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[7][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[7][company_name]").send_keys("HESS")
    # self.driver.find_element(By.NAME, "assets[7][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[7][account_number]").send_keys("1865")
    # self.driver.find_element(By.NAME, "assets[7][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[7][unpaid_balance]").send_keys("750")
    self.driver.find_element(By.NAME, "liabilities[7][monthly_payment]").send_keys("36")
    Select(self.driver.find_element(By.NAME, "liabilities[7][to_be_paid_off]")).select_by_value('false')

        ###### 7th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[8][account_type]")).select_by_value('INSTALLMENT (e.g., car, student, personal loans)') 
    self.driver.find_element(By.NAME, "liabilities[8][company_name]").send_keys("Kentucky Telco")
    # self.driver.find_element(By.NAME, "assets[8][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[8][account_number]").send_keys("9743227")
    # self.driver.find_element(By.NAME, "assets[8][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[8][unpaid_balance]").send_keys("255")
    self.driver.find_element(By.NAME, "liabilities[8][monthly_payment]").send_keys("15")
    Select(self.driver.find_element(By.NAME, "liabilities[8][to_be_paid_off]")).select_by_value('false')

        ###### 7th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[9][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[9][company_name]").send_keys("MBNA America")
    # self.driver.find_element(By.NAME, "assets[9][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[9][account_number]").send_keys("64483")
    # self.driver.find_element(By.NAME, "assets[9][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[9][unpaid_balance]").send_keys("200")
    self.driver.find_element(By.NAME, "liabilities[9][monthly_payment]").send_keys("50")
    Select(self.driver.find_element(By.NAME, "liabilities[9][to_be_paid_off]")).select_by_value('false')

    self.driver.find_element(By.ID, "kyc_next_button").click()

####################################


    # Step 17 Tell us about your property.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "real_estates[0][street]")))
    self.driver.find_element(By.NAME, "real_estates[0][street]").send_keys("30782 Rolling Road")
    self.driver.find_element(By.NAME, "real_estates[0][city]").send_keys("Louisville")
    self.driver.find_element(By.NAME, "real_estates[0][state]").send_keys("KY")
    self.driver.find_element(By.NAME, "real_estates[0][zipcode]").send_keys("40207")
    self.driver.find_element(By.NAME, "real_estates[0][property_value]").send_keys("575000")
    self.driver.find_element(By.NAME, "real_estates[0][monthly_insurance]").send_keys("223")
    Select(self.driver.find_element(By.NAME, "real_estates[0][property_type]")).select_by_value('SFR')
    Select(self.driver.find_element(By.NAME, "real_estates[0][status]")).select_by_value('RETAINED')
    Select(self.driver.find_element(By.NAME, "real_estates[0][occupancy]")).select_by_value('IP')
    Select(self.driver.find_element(By.NAME, "real_estates[0][intended_occupancy]")).select_by_value('PR')

    self.driver.find_element(By.ID, "add_mortgage_0").click()
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][creditor_name]").send_keys('Kentucky National')
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][account_number]").send_keys('1234567')
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][monthly_mortgage_payment]").send_keys('817')
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][unpaid_balance]").send_keys('123773')
    Select(self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][type]")).select_by_value('CONVENTIONAL')

    self.driver.find_element(By.ID, "kyc_next_button").click()
####################################
    # Step 18 Let's find out more about your mortgage.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.ID, "knockout_question_abaa6b6e-5848-453a-86d5-399a24095565_true").click()
    self.driver.find_element(By.ID, "knockout_question_84298507-f2af-4e3f-82ab-dd95493d8609_true").click()
    self.driver.find_element(By.ID, "knockout_question_0611261b-930d-45d0-82c5-b53086c4089b_true").click()
    self.driver.find_element(By.ID, "knockout_question_f063e3ca-615b-4890-a857-e3ffc3be99dd_true").click()
    self.driver.find_element(By.ID, "knockout_question_678d4839-ebc9-4619-8493-956ee84ad8db_true").click()
    self.driver.find_element(By.ID, "knockout_question_bc420287-f293-40f3-a95e-a0b23251533f_true").click()
    self.driver.find_element(By.ID, "knockout_question_a3d6c394-9bd0-4c52-8f9a-281e2f40a708_true").click()
    self.driver.find_element(By.ID, "knockout_question_8256e274-a711-4ade-bf4d-e5475a5f5a1c_true").click()
    self.driver.find_element(By.ID, "knockout_question_536878d0-8c8b-4df9-b559-b9b4f27b94de_true").click()
    self.driver.find_element(By.ID, "knockout_question_d9488456-76d7-4c87-8096-498ffc6d58bb_true").click()
    self.driver.find_element(By.ID, "knockout_question_36203b63-6f41-40fd-89bc-966f83c8e262_true").click()
    self.driver.find_element(By.ID, "knockout_question_37b917ac-4754-47a7-bba0-6e76c67b5cb9_true").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()



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
    Select(self.driver.find_element(By.NAME, "property_address[your_asset]")).select_by_index(0)

    Select(self.driver.find_element(By.NAME, "property_address[occupancy]")).select_by_value('PR')
    Select(self.driver.find_element(By.NAME, "property_address[property_type]")).select_by_value('SFR')
    Select(self.driver.find_element(By.NAME, "property_address[estate_type]")).select_by_value('FEE SIMPLE')

    self.driver.find_element(By.ID, "property_in_project_false").click()
    self.driver.find_element(By.ID, "mix_usage_false").click()
    self.driver.find_element(By.ID, "clean_energy_lien_false").click()
    self.driver.find_element(By.ID, "contract_for_deed_false").click()
    self.driver.find_element(By.ID, "energy_related_improvement_false").click()

    # expense
    self.driver.find_element(By.ID, "add_expense").click()
    Select(self.driver.find_element(By.NAME, "expenses[0][type]")).select_by_value('FIRST MORTGAGE PRINCIPAL AND INTEREST')
    self.driver.find_element(By.NAME, "expenses[0][amount]").send_keys("506.69")

    self.driver.find_element(By.ID, "add_expense").click()
    Select(self.driver.find_element(By.NAME, "expenses[1][type]")).select_by_value('HOME OWNERS INSURANCE')
    self.driver.find_element(By.NAME, "expenses[1][amount]").send_keys("153")

    self.driver.find_element(By.ID, "add_expense").click()
    Select(self.driver.find_element(By.NAME, "expenses[2][type]")).select_by_value('REAL ESTATE TAX')
    self.driver.find_element(By.NAME, "expenses[2][amount]").send_keys("188")

    self.driver.find_element(By.ID, "add_expense").click()
    Select(self.driver.find_element(By.NAME, "expenses[3][type]")).select_by_value('OTHER MORTGAGE LOAN PRINCIPAL AND INTEREST')
    self.driver.find_element(By.NAME, "expenses[3][amount]").send_keys("0")
    
    self.driver.find_element(By.NAME, "property_address[refinance_debt]").send_keys("211833")
    self.driver.find_element(By.NAME, "property_address[loan_amount]").send_keys("220000")
    self.driver.find_element(By.NAME, "property_address[estimated_net]").send_keys("0")
    self.driver.find_element(By.NAME, "property_address[estimated_gross]").send_keys("0")
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
  

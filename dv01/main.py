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
    self.driver.find_element(By.ID, "email").send_keys("dv01test3@mail.com") # maindv01@mail.com testdv01@mail.com/ Test1234= mainjohndv01@mail.com/Main1234= #dv01test1@mail.com/Dv011234=
    self.driver.find_element(By.ID, "password").send_keys("Main1234=")  # Main1234=   Dv011234=
    self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[1]/form/div[3]/div[3]/button").click()

    # #Authentication Pro
    # element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "code")))
    # element.send_keys("654508")
    # self.driver.find_element(By.CSS_SELECTOR, ".bg-trueblok-primary").click()

######################################

    # Start KYC
    kyctrigger = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div[2]/a")))
    kyctrigger.click()
######################################

    # Step 00 Loan Purpose
    # loanpurpose = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "loan_purpose_purchase_button"))) #loan_purpose_refinance_button
    # loanpurpose.click()
    # loanjoint = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "type_of_credit_joint_button")))
    # loanjoint.click()    

    # Select(self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[2]/select")).select_by_value('1')
    # self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[3]/div/div/input[2]").send_keys("comarydv01@mail.com")

    # self.driver.find_elements(By.ID, "continue_button").click()
#####################################

#     # Step 01 Full name
#     fname = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[first_name]")))
#     if fname.get_attribute('value') == None:
#         fname.send_keys("John")
#     else:
#         fname.clear()
#         fname.send_keys("John")

#     lname = self.driver.find_element(By.NAME, "kyc[last_name]")
#     if lname.get_attribute('value') == None:
#         lname.send_keys("Freddie")
#     else:
#         lname.clear()
#         lname.send_keys("Freddie")

#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 02 Birth Date
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][0]")).select_by_value('DECEMBER')
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][1]")).select_by_value('23')
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][2]")).select_by_value('1963')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 03 Gender
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     Select(self.driver.find_element(By.NAME, "kyc[gender]")).select_by_value('MALE')
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
#     Select(self.driver.find_element(By.NAME, "kyc[marital_status]")).select_by_value('MARRIED')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# ####################################

#     # Step 07 SSN
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "ssn_number")))

#     ssn = self.driver.find_element(By.ID, "ssn_number")
#     if ssn.get_attribute('value') == None:
#         ssn.send_keys("990-10-0001")
#     else:
#         ssn.clear()
#         ssn.send_keys("990-10-0001")
#     # self.driver.find_element(By.ID, "ssn_number").send_keys("990-01-0001")
#     self.driver.find_element(By.CSS_SELECTOR, ".fa-2x").click()
#     self.driver.find_element(By.ID, "kyc_step7_next_button").click()
# #####################################

#     # Step 08 Phone Number
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[home_phone_number]")))
#     self.driver.find_element(By.NAME, "kyc[home_phone_number]").clear()
#     self.driver.find_element(By.NAME, "kyc[home_phone_number]").send_keys("(202) 222-2222" ) #Home 
#     self.driver.find_element(By.NAME, "kyc[cell_phone_number]").clear()
#     self.driver.find_element(By.NAME, "kyc[cell_phone_number]").send_keys("(202) 333-3333") #Cell
#     self.driver.find_element(By.NAME, "kyc[work_phone_number]").clear()
#     self.driver.find_element(By.NAME, "kyc[work_phone_number]").send_keys("(202) 444-4444") #Work
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 09 Current Address
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "current_address[street]")))
#     self.driver.find_element(By.NAME, "current_address[street]").clear()
#     self.driver.find_element(By.NAME, "current_address[street]").send_keys("175 13th Street")
#     self.driver.find_element(By.NAME, "current_address[city]").clear()
#     self.driver.find_element(By.NAME, "current_address[city]").send_keys("Washington")
#     self.driver.find_element(By.NAME, "current_address[zipcode]").clear()
#     self.driver.find_element(By.NAME, "current_address[zipcode]").send_keys("20013")
#     Select(self.driver.find_element(By.NAME, "current_address[years]")).select_by_value('16')
#     Select(self.driver.find_element(By.NAME, "current_address[months]")).select_by_value('4')
#     Select(self.driver.find_element(By.NAME, "current_address[housing]")).select_by_value('OWN')
#     self.driver.find_element(By.NAME, "current_address[rent_per_month]").clear()
#     self.driver.find_element(By.NAME, "current_address[rent_per_month]").send_keys("1950")
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 10 Mailing Address
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label/input[2]")))
#     check = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label/input[2]")
#     # if check.is_selected()  == True:
#     #     check.click()
#     #     check.click()
#     # else:
#     check.click()
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################
   
#     # Step 11 served army
#     military = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_military_service_false")))
#     military.click()
#     self.driver.find_element(By.ID, "kyc_next_button").click()
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
#     self.driver.find_element(By.NAME, "current_employments[0][employer_name]").send_keys("Enterprise One")
#     self.driver.find_element(By.NAME, "current_employments[0][position]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][position]").send_keys("Manager")
#     self.driver.find_element(By.NAME, "current_employments[0][phone]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][phone]").send_keys("8003214567")
#     self.driver.find_element(By.NAME, "current_employments[0][street]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][street]").send_keys("1234 Sweet Tea Ln")
#     self.driver.find_element(By.NAME, "current_employments[0][city]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][city]").send_keys("McLean")
#     self.driver.find_element(By.NAME, "current_employments[0][state]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][state]").send_keys("VA")
#     self.driver.find_element(By.NAME, "current_employments[0][zipcode]").clear()
#     self.driver.find_element(By.NAME, "current_employments[0][zipcode]").send_keys("220212")
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][0]")).select_by_value('DECEMBER')
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][1]")).select_by_value('12')
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][2]")).select_by_value('1999')

#     self.driver.find_element(By.ID, "add_current_employment_income_0").click()
#     self.driver.find_element(By.NAME, "current_employments[0][base_income]").send_keys("4240")
#     self.driver.find_element(By.NAME, "current_employments[0][bonus]").send_keys("500")

#     self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 16 Tell us about your assets.
        ####### 1st asset #######
    WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[0][account_type]")).select_by_value('SAVINGS') 
    # self.driver.find_element(By.NAME, "assets[0][financial_institution]").click()
    self.driver.find_element(By.NAME, "assets[0][financial_institution]").send_keys("BankA")
    # self.driver.find_element(By.NAME, "assets[0][account_number]").click()
    self.driver.find_element(By.NAME, "assets[0][account_number]").send_keys("1523421245")
    # self.driver.find_element(By.NAME, "assets[0][market_value]").click()
    self.driver.find_element(By.NAME, "assets[0][market_value]").send_keys("45000")

        ####### 2nd asset #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[1][account_type]")).select_by_value('CHECKING') 
    self.driver.find_element(By.NAME, "assets[1][financial_institution]").send_keys("FinBank Profiles - A")
    # self.driver.find_element(By.NAME, "assets[1][account_number]").click()
    self.driver.find_element(By.NAME, "assets[1][account_number]").send_keys("9012")
    # self.driver.find_element(By.NAME, "assets[1][market_value]").click()
    self.driver.find_element(By.NAME, "assets[1][market_value]").send_keys("10000")

        ####### 3rd asset #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[2][account_type]")).select_by_value('MONEY MARKET FUND') 
    self.driver.find_element(By.NAME, "assets[2][financial_institution]").send_keys("BVD")
    # self.driver.find_element(By.NAME, "assets[2][account_number]").click()
    self.driver.find_element(By.NAME, "assets[2][account_number]").send_keys("6239")
    # self.driver.find_element(By.NAME, "assets[2][market_value]").click()
    self.driver.find_element(By.NAME, "assets[2][market_value]").send_keys("37000")

        ####### 4th asset #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[3][account_type]")).select_by_value('MUTUAL FUND') 
    self.driver.find_element(By.NAME, "assets[3][financial_institution]").send_keys("ANP")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "assets[3][account_number]").send_keys("492335")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "assets[3][market_value]").send_keys("61000")

        ####### 1st other asset #######
    self.driver.find_element(By.ID, "btn_add__other_asset").click()
    Select(self.driver.find_element(By.NAME, "other_assets[0][asset_type]")).select_by_value('DIVIDENDS INTEREST') #capitalgain
    self.driver.find_element(By.NAME, "other_assets[0][market_value]").send_keys("253")

        ####### 2nd other asset #######
    self.driver.find_element(By.ID, "btn_add__other_asset").click()
    Select(self.driver.find_element(By.NAME, "other_assets[1][asset_type]")).select_by_value('CAPITAL GAINS') #capitalgain
    self.driver.find_element(By.NAME, "other_assets[1][market_value]").send_keys("1000")

        ###### 4th other asset #######
    self.driver.find_element(By.ID, "btn_add__other_asset").click()
    Select(self.driver.find_element(By.NAME, "other_assets[2][asset_type]")).select_by_value('PROCEEDS FROM SALE OF REAL ESTATE ASSET') 
    self.driver.find_element(By.NAME, "other_assets[2][market_value]").send_keys("284365")

        ###### 1st liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[0][account_type]")).select_by_value('INSTALLMENT (e.g., car, student, personal loans)') 
    self.driver.find_element(By.NAME, "liabilities[0][company_name]").send_keys("TOYOTA CREDIT")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[0][account_number]").send_keys("913432")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[0][unpaid_balance]").send_keys("15838")
    self.driver.find_element(By.NAME, "liabilities[0][monthly_payment]").send_keys("500")
    Select(self.driver.find_element(By.NAME, "liabilities[0][to_be_paid_off]")).select_by_value('false')

        ###### 2nd liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[1][account_type]")).select_by_value('INSTALLMENT (e.g., car, student, personal loans)') 
    self.driver.find_element(By.NAME, "liabilities[1][company_name]").send_keys("CHASE")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[1][account_number]").send_keys("8745698")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[1][unpaid_balance]").send_keys("1799")
    self.driver.find_element(By.NAME, "liabilities[1][monthly_payment]").send_keys("257")
    Select(self.driver.find_element(By.NAME, "liabilities[1][to_be_paid_off]")).select_by_value('false')

        ###### 3rd liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[2][account_type]")).select_by_value('INSTALLMENT (e.g., car, student, personal loans)') 
    self.driver.find_element(By.NAME, "liabilities[2][company_name]").send_keys("Sallie Mae")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[2][account_number]").send_keys("258741")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[2][unpaid_balance]").send_keys("5000")
    self.driver.find_element(By.NAME, "liabilities[2][monthly_payment]").send_keys("12")
    Select(self.driver.find_element(By.NAME, "liabilities[2][to_be_paid_off]")).select_by_value('false')

        ###### 4th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[3][account_type]")).select_by_value('INSTALLMENT (e.g., car, student, personal loans)') 
    self.driver.find_element(By.NAME, "liabilities[3][company_name]").send_keys("Sallie Mae")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[3][account_number]").send_keys("21478521")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[3][unpaid_balance]").send_keys("1100")
    self.driver.find_element(By.NAME, "liabilities[3][monthly_payment]").send_keys("25")
    Select(self.driver.find_element(By.NAME, "liabilities[3][to_be_paid_off]")).select_by_value('false')

        ###### 5th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[4][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[4][company_name]").send_keys("Universal Visa")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[4][account_number]").send_keys("325792")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[4][unpaid_balance]").send_keys("125")
    self.driver.find_element(By.NAME, "liabilities[4][monthly_payment]").send_keys("25")
    Select(self.driver.find_element(By.NAME, "liabilities[4][to_be_paid_off]")).select_by_value('false')
    
        ###### 6th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[5][account_type]")).select_by_value('MORTGAGE LOAN') 
    self.driver.find_element(By.NAME, "liabilities[5][company_name]").send_keys("ABC Lending")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[5][account_number]").send_keys("7981421")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[5][unpaid_balance]").send_keys("300000")
    self.driver.find_element(By.NAME, "liabilities[5][monthly_payment]").send_keys("1950")
    Select(self.driver.find_element(By.NAME, "liabilities[5][to_be_paid_off]")).select_by_value('false')

        ###### 7th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[6][account_type]")).select_by_value('OPEN 30-DAY (balance paid monthly)') 
    self.driver.find_element(By.NAME, "liabilities[6][company_name]").send_keys("AMEX")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[6][account_number]").send_keys("6011452244482")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[6][unpaid_balance]").send_keys("1527")
    self.driver.find_element(By.NAME, "liabilities[6][monthly_payment]").send_keys("1527")
    Select(self.driver.find_element(By.NAME, "liabilities[6][to_be_paid_off]")).select_by_value('false')

        ###### 1st other liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_other_liability_btn")))
    self.driver.find_element(By.ID, "add_other_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "other_liabilities[0][liability_type]")).select_by_value('JOB RELATED EXPENSES') 
    self.driver.find_element(By.NAME, "other_liabilities[0][market_value]").send_keys("127")

        ###### 2nd other liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_other_liability_btn")))
    self.driver.find_element(By.ID, "add_other_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "other_liabilities[1][liability_type]")).select_by_value('CHILD SUPPORT') 
    self.driver.find_element(By.NAME, "other_liabilities[1][market_value]").send_keys("500")

        ###### 3rd other liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_other_liability_btn")))
    self.driver.find_element(By.ID, "add_other_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "other_liabilities[2][liability_type]")).select_by_value('SEPARATE MAINTENANCE') 
    self.driver.find_element(By.NAME, "other_liabilities[2][market_value]").send_keys("359")

    self.driver.find_element(By.ID, "kyc_next_button").click()

#####################################


    # Step 17 Tell us about your property.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_real_estate_true")))
    self.driver.find_element(By.ID, "kyc_real_estate_true").click()

    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "real_estates[0][street]")))
    self.driver.find_element(By.NAME, "real_estates[0][street]").send_keys("175 13th Street")
    self.driver.find_element(By.NAME, "real_estates[0][city]").send_keys("Washington")
    self.driver.find_element(By.NAME, "real_estates[0][state]").send_keys("DC")
    self.driver.find_element(By.NAME, "real_estates[0][zipcode]").send_keys("20013")
    self.driver.find_element(By.NAME, "real_estates[0][property_value]").send_keys("550000")
    self.driver.find_element(By.NAME, "real_estates[0][monthly_insurance]").send_keys("635")
    Select(self.driver.find_element(By.NAME, "real_estates[0][property_type]")).select_by_value('SFR')
    Select(self.driver.find_element(By.NAME, "real_estates[0][status]")).select_by_value('PENDING SALE')
    Select(self.driver.find_element(By.NAME, "real_estates[0][occupancy]")).select_by_value('PR')
    Select(self.driver.find_element(By.NAME, "real_estates[0][intended_occupancy]")).select_by_value('PR')

    self.driver.find_element(By.ID, "add_mortgage_0").click()
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][creditor_name]").send_keys('ABC Lending')
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][account_number]").send_keys('7891421')
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][monthly_mortgage_payment]").send_keys('1950')
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][unpaid_balance]").send_keys('300000')
    Select(self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][type]")).select_by_value('CONVENTIONAL')

    self.driver.find_element(By.ID, "add_additional_property").click()

    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "real_estates[1][street]")))
    self.driver.find_element(By.NAME, "real_estates[1][street]").send_keys("1234 Country Street")
    self.driver.find_element(By.NAME, "real_estates[1][city]").send_keys("Rehobeth")
    self.driver.find_element(By.NAME, "real_estates[1][state]").send_keys("DW")
    self.driver.find_element(By.NAME, "real_estates[1][zipcode]").send_keys("19971")
    self.driver.find_element(By.NAME, "real_estates[1][property_value]").send_keys("150000")
    self.driver.find_element(By.NAME, "real_estates[1][monthly_insurance]").send_keys("575")
    Select(self.driver.find_element(By.NAME, "real_estates[1][property_type]")).select_by_value('SFR')
    Select(self.driver.find_element(By.NAME, "real_estates[1][status]")).select_by_value('RETAINED')
    Select(self.driver.find_element(By.NAME, "real_estates[1][occupancy]")).select_by_value('SH')
    Select(self.driver.find_element(By.NAME, "real_estates[1][intended_occupancy]")).select_by_value('SH')
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
    self.driver.find_element(By.NAME, "property_address[street]").click()
    self.driver.find_element(By.NAME, "property_address[street]").send_keys("1234 Main Street")
    self.driver.find_element(By.NAME, "property_address[state]").click()
    self.driver.find_element(By.NAME, "property_address[state]").send_keys("NC")
    self.driver.find_element(By.NAME, "property_address[city]").click()
    self.driver.find_element(By.NAME, "property_address[city]").send_keys("Winston Salem")
    self.driver.find_element(By.NAME, "property_address[zipcode]").click()
    self.driver.find_element(By.NAME, "property_address[zipcode]").send_keys("27104")
    Select(self.driver.find_element(By.NAME, "property_address[occupancy]")).select_by_value('PR')
    Select(self.driver.find_element(By.NAME, "property_address[property_type]")).select_by_value('SFR')


    self.driver.find_element(By.ID, "property_in_project_false").click()
    self.driver.find_element(By.ID, "mix_usage_false").click()
    self.driver.find_element(By.ID, "clean_energy_lien_false").click()

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

    self.driver.find_element(By.NAME, "property_address[loan_amount]").send_keys("100000")

    self.driver.find_element(By.ID, "kyc_next_button").click()
####################################

    # Step 24 Docusign
  
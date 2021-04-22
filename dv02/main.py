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
    self.driver.find_element(By.ID, "email").send_keys("mainandydv02test2@mail.com") # maindv01@mail.com #mainandydv02@mail.com
    self.driver.find_element(By.ID, "password").send_keys("Main1234=")  # Main1234=
    self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[1]/form/div[3]/div[3]/button").click()
######################################

    # Start KYC
    kyctrigger = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div[2]/a")))
    kyctrigger.click()
######################################

    # Step 00 Loan Purpose
    loanpurpose = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "loan_purpose_refinance_button"))) #loan_purpose_purchase_button
    loanpurpose.click()
    loanjoint = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "type_of_credit_joint_button")))
    loanjoint.click()    
    Select(self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[2]/select")).select_by_value('1')
    self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[3]/div/div/input[2]").send_keys("amycodv02@mail.com")

    self.driver.find_element(By.ID, "continue_button").click()
#####################################

    # Step 01 Full name
    name = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[first_name]")))

    if name.get_attribute('value') == None:
        name.send_keys("Andy")
    else:
        self.driver.find_element(By.NAME, "kyc[first_name]").clear()
        self.driver.find_element(By.NAME, "kyc[first_name]").send_keys("Andy")

    lname = self.driver.find_element(By.NAME, "kyc[last_name]")
    if lname.get_attribute('value') == None :
        lname.send_keys("Freddie")
    else:
        lname.clear()
        lname.send_keys("Freddie")

    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 02 Birth Date
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][0]")).select_by_value('JUNE')
    Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][1]")).select_by_value('30')
    Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][2]")).select_by_value('1971')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 03 Gender
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    Select(self.driver.find_element(By.NAME, "kyc[gender]")).select_by_value('MALE')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 04 Dependents
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[dependents_number]")))
    Select(self.driver.find_element(By.NAME, "kyc[dependents_number]")).select_by_value('0')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 05 Citizenship
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[citizenship]")))
    Select(self.driver.find_element(By.NAME, "kyc[citizenship]")).select_by_value('U.S. CITIZEN')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 06 Marital Status
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[marital_status]")))
    Select(self.driver.find_element(By.NAME, "kyc[marital_status]")).select_by_value('MARRIED')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 07 SSN
    ssn = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "ssn_number")))
    if ssn.get_attribute('value') == None:
        self.driver.find_element(By.ID, "ssn_number").send_keys("990-30-0003")
    else:
        self.driver.find_element(By.ID, "ssn_number").clear()
        self.driver.find_element(By.ID, "ssn_number").send_keys("990-30-0003")

    self.driver.find_element(By.CSS_SELECTOR, ".fa-2x").click()
    self.driver.find_element(By.ID, "kyc_step7_next_button").click()
#####################################

    # Step 08 Phone Number
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[home_phone_number]")))

    # self.driver.find_element(By.NAME, "kyc[home_phone_number]").click()
    home_phone = self.driver.find_element(By.NAME, "kyc[home_phone_number]")
    if home_phone.get_attribute('value') == None:
        home_phone.send_keys("(555) 222-2222" ) #Home 
    else:
        home_phone.clear()
        home_phone.send_keys("(555) 222-2222" ) #Home
        
    cell_phone = self.driver.find_element(By.NAME, "kyc[cell_phone_number]")
    if cell_phone.get_attribute('value') == None:
        cell_phone.send_keys("(555) 333-3333" ) #Home 
    else:
        cell_phone.clear()
        cell_phone.send_keys("(555) 333-3333" ) #Home 

    self.driver.find_element(By.NAME, "kyc[work_phone_number]").clear() #Work
    self.driver.find_element(By.NAME, "kyc[work_phone_number]").send_keys("(555) 444-4444") #Work
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 09 Current Address
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "current_address[street]")))
    self.driver.find_element(By.NAME, "current_address[street]").clear()
    self.driver.find_element(By.NAME, "current_address[street]").send_keys("4321 Cul de Sac Street")
    self.driver.find_element(By.NAME, "current_address[city]").clear()
    self.driver.find_element(By.NAME, "current_address[city]").send_keys("Someplace")
    self.driver.find_element(By.NAME, "current_address[zipcode]").clear()
    self.driver.find_element(By.NAME, "current_address[zipcode]").send_keys("02723")
    # self.driver.find_element(By.NAME, "current_address[years]").click()
    Select(self.driver.find_element(By.NAME, "current_address[years]")).select_by_value('7')
    Select(self.driver.find_element(By.NAME, "current_address[months]")).select_by_value('11')
    Select(self.driver.find_element(By.NAME, "current_address[housing]")).select_by_value('OWN')
    self.driver.find_element(By.NAME, "current_address[rent_per_month]").clear()
    self.driver.find_element(By.NAME, "current_address[rent_per_month]").send_keys("1950")
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 10 Mailing Address
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label/input[2]")))
    check = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label/input[2]")
    if check.is_selected() == True:
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label/input[2]").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label/input[2]").click()
    else:
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label/input[2]").click()

    
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################
   
    # Step 11 served army
    military = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_military_service_true")))
    military.click()

    self.driver.find_element(By.CSS_SELECTOR, "div.shadow:nth-child(2) > fieldset:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(3)").click()

    Select(self.driver.find_element(By.NAME, "kyc[military_currently_serving_expiration_year]")).select_by_value('29')
    Select(self.driver.find_element(By.NAME, "kyc[military_currently_serving_expiration_month]")).select_by_value('0')
    self.driver.find_element(By.NAME, "militaryIncome[military_division]").send_keys("US Army Reserve")
    Select(self.driver.find_element(By.NAME, "militaryIncome[start_date][0]")).select_by_value('AUGUST')
    Select(self.driver.find_element(By.NAME, "militaryIncome[start_date][1]")).select_by_value('5')
    Select(self.driver.find_element(By.NAME, "militaryIncome[start_date][2]")).select_by_value('2010')

    self.driver.find_element(By.ID, "add_military_income").click()
    self.driver.find_element(By.NAME, "militaryIncome[base_income]").send_keys("629")
    self.driver.find_element(By.NAME, "militaryIncome[rations_allowance]").send_keys("100")
    self.driver.find_element(By.NAME, "militaryIncome[clothes_allowance]").send_keys("65")


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
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "current_employments[0][employer_name]")))

    self.driver.find_element(By.NAME, "current_employments[0][employer_name]").send_keys("Veterans Advocacy of Massachusets")
    self.driver.find_element(By.NAME, "current_employments[0][position]").clear()
    self.driver.find_element(By.NAME, "current_employments[0][position]").send_keys("Owner")
    self.driver.find_element(By.NAME, "current_employments[0][phone]").clear()
    self.driver.find_element(By.NAME, "current_employments[0][phone]").send_keys("8003214567")
    self.driver.find_element(By.NAME, "current_employments[0][street]").clear()
    self.driver.find_element(By.NAME, "current_employments[0][street]").send_keys("1234 Sweet Tea Ln")
    self.driver.find_element(By.NAME, "current_employments[0][city]").clear()
    self.driver.find_element(By.NAME, "current_employments[0][city]").send_keys("Someplace")
    self.driver.find_element(By.NAME, "current_employments[0][state]").clear()
    self.driver.find_element(By.NAME, "current_employments[0][state]").send_keys("MA")
    self.driver.find_element(By.NAME, "current_employments[0][zipcode]").clear()
    self.driver.find_element(By.NAME, "current_employments[0][zipcode]").send_keys("02723")
    Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][2]")).select_by_value('2011')
    Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][0]")).select_by_value('JULY')
    Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][1]")).select_by_value('4')

    self.driver.find_element(By.NAME, "current_employments[0][base_income]").clear()
    self.driver.find_element(By.NAME, "current_employments[0][base_income]").send_keys("7500")
    self.driver.find_element(By.CSS_SELECTOR, "div.flex:nth-child(8) > div:nth-child(1) > label:nth-child(1) > div:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "label.trueblok-radio:nth-child(2) > span:nth-child(2)").click()
    self.driver.find_element(By.NAME, "current_employments[0][business_owner_monthly_income]").send_keys("7500")

    self.driver.find_element(By.ID, "add_another_job_button").click()
    self.driver.find_element(By.NAME, "current_employments[1][employer_name]").send_keys("US Army Reserve")
    self.driver.find_element(By.NAME, "current_employments[1][position]").clear()
    self.driver.find_element(By.NAME, "current_employments[1][position]").send_keys("Lieutenant")
    self.driver.find_element(By.NAME, "current_employments[1][phone]").clear()
    self.driver.find_element(By.NAME, "current_employments[1][phone]").send_keys("8007792399")
    # self.driver.find_element(By.NAME, "current_employments[1][street]").click()
    self.driver.find_element(By.NAME, "current_employments[1][street]").send_keys("2400 Army Barracks Street")
    # self.driver.find_element(By.NAME, "current_employments[1][city]").click()
    self.driver.find_element(By.NAME, "current_employments[1][city]").send_keys("Someplace")
    # self.driver.find_element(By.NAME, "current_employments[1][state]").click()
    self.driver.find_element(By.NAME, "current_employments[1][state]").send_keys("MA")
    # self.driver.find_element(By.NAME, "current_employments[1][zipcode]").click()
    self.driver.find_element(By.NAME, "current_employments[1][zipcode]").send_keys("02723")
    # self.driver.find_element(By.NAME, "current_employments[0][start_date][0]").click()
    Select(self.driver.find_element(By.NAME, "current_employments[1][start_date][0]")).select_by_value('AUGUST')
    Select(self.driver.find_element(By.NAME, "current_employments[1][start_date][1]")).select_by_value('5')
    Select(self.driver.find_element(By.NAME, "current_employments[1][start_date][2]")).select_by_value('2010')
    self.driver.find_element(By.NAME, "current_employments[1][base_income]").send_keys("629")

    # self.driver.find_element(By.NAME, "current_employments[1][base_income]").click()


    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 16 Tell us about your assets.
        ####### 1st asset #######

    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[0][account_type]")).select_by_value('CHECKING') 
    self.driver.find_element(By.NAME, "assets[0][financial_institution]").send_keys("Dag Site")
    # self.driver.find_element(By.NAME, "assets[0][account_number]").click()
    self.driver.find_element(By.NAME, "assets[0][account_number]").send_keys("109024")
    # self.driver.find_element(By.NAME, "assets[0][market_value]").click()
    self.driver.find_element(By.NAME, "assets[0][market_value]").send_keys("36000")

        ####### 2nd asset #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[1][account_type]")).select_by_value('SAVINGS') 
    self.driver.find_element(By.NAME, "assets[1][financial_institution]").send_keys("FinBank Profiles - A")
    # self.driver.find_element(By.NAME, "assets[1][account_number]").click()
    self.driver.find_element(By.NAME, "assets[1][account_number]").send_keys("9018")
    # self.driver.find_element(By.NAME, "assets[1][market_value]").click()
    self.driver.find_element(By.NAME, "assets[1][market_value]").send_keys("20000")

        ####### 3rd asset #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[2][account_type]")).select_by_value('SAVINGS') 
    self.driver.find_element(By.NAME, "assets[2][financial_institution]").send_keys("EZ INVESTMENTS")
    # self.driver.find_element(By.NAME, "assets[2][account_number]").click()
    self.driver.find_element(By.NAME, "assets[2][account_number]").send_keys("8523698")
    # self.driver.find_element(By.NAME, "assets[2][market_value]").click()
    self.driver.find_element(By.NAME, "assets[2][market_value]").send_keys("756897")

        ####### 4th asset #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[3][account_type]")).select_by_value('RETIREMENT (e.g., 401k, IRA)') 
    self.driver.find_element(By.NAME, "assets[3][financial_institution]").send_keys("Veteran Savings Group")
    self.driver.find_element(By.NAME, "assets[3][account_number]").send_keys("45745")
    self.driver.find_element(By.NAME, "assets[3][market_value]").send_keys("950000")
        ####### 5th asset #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "btn_add_asset")))
    self.driver.find_element(By.ID, "btn_add_asset").click()
    Select(self.driver.find_element(By.NAME, "assets[4][account_type]")).select_by_value('CASH VALUE OF LIFE INSURANCE (USED FOR THE TRANSACTION)') 
    self.driver.find_element(By.NAME, "assets[4][financial_institution]").send_keys("USAA")
    self.driver.find_element(By.NAME, "assets[4][account_number]").send_keys("741113")
    self.driver.find_element(By.NAME, "assets[4][market_value]").send_keys("32000")

        ###### 1st liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[0][account_type]")).select_by_value('MORTGAGE LOAN') 
    self.driver.find_element(By.NAME, "liabilities[0][company_name]").send_keys("Best Ever Mortgage")
    self.driver.find_element(By.NAME, "liabilities[0][account_number]").send_keys("87412457")
    self.driver.find_element(By.NAME, "liabilities[0][unpaid_balance]").send_keys("210279")
    self.driver.find_element(By.NAME, "liabilities[0][monthly_payment]").send_keys("1691")
    Select(self.driver.find_element(By.NAME, "liabilities[0][to_be_paid_off]")).select_by_value('true')

        ###### 2nd liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[1][account_type]")).select_by_value('MORTGAGE LOAN') 
    self.driver.find_element(By.NAME, "liabilities[1][company_name]").send_keys("Callable Mortgage")
    self.driver.find_element(By.NAME, "liabilities[1][account_number]").send_keys("987411547")
    self.driver.find_element(By.NAME, "liabilities[1][unpaid_balance]").send_keys("210027")
    self.driver.find_element(By.NAME, "liabilities[1][monthly_payment]").send_keys("1671")
    Select(self.driver.find_element(By.NAME, "liabilities[1][to_be_paid_off]")).select_by_value('false')

        ###### 3rd liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[2][account_type]")).select_by_value('HELOC') 
    self.driver.find_element(By.NAME, "liabilities[2][company_name]").send_keys("Flying Dollar Mortgage")
    self.driver.find_element(By.NAME, "liabilities[2][account_number]").send_keys("75142341")
    self.driver.find_element(By.NAME, "liabilities[2][unpaid_balance]").send_keys("45")
    self.driver.find_element(By.NAME, "liabilities[2][monthly_payment]").send_keys("40")
    Select(self.driver.find_element(By.NAME, "liabilities[2][to_be_paid_off]")).select_by_value('false')

        ###### 4th liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_liability_btn")))
    self.driver.find_element(By.ID, "add_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "liabilities[3][account_type]")).select_by_value('REVOLVING (e.g., credit cards)') 
    self.driver.find_element(By.NAME, "liabilities[3][company_name]").send_keys("Relentless Bank")
    # self.driver.find_element(By.NAME, "assets[3][account_number]").click()
    self.driver.find_element(By.NAME, "liabilities[3][account_number]").send_keys("85746187")
    # self.driver.find_element(By.NAME, "assets[3][market_value]").click()
    self.driver.find_element(By.NAME, "liabilities[3][unpaid_balance]").send_keys("29")
    self.driver.find_element(By.NAME, "liabilities[3][monthly_payment]").send_keys("10")
    Select(self.driver.find_element(By.NAME, "liabilities[3][to_be_paid_off]")).select_by_value('false')

        ###### 1st other liability #######
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "add_other_liability_btn")))
    self.driver.find_element(By.ID, "add_other_liability_btn").click()
    Select(self.driver.find_element(By.NAME, "other_liabilities[0][liability_type]")).select_by_value('CHILD SUPPORT') 
    self.driver.find_element(By.NAME, "other_liabilities[0][market_value]").send_keys("250")
    self.driver.find_element(By.ID, "kyc_next_button").click()

#####################################


    # Step 17 Tell us about your property.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "real_estates[0][street]")))
    self.driver.find_element(By.NAME, "real_estates[0][street]").send_keys("4321 Cul de Sac Street")
    self.driver.find_element(By.NAME, "real_estates[0][city]").send_keys("Someplace")
    self.driver.find_element(By.NAME, "real_estates[0][state]").send_keys("MA")
    self.driver.find_element(By.NAME, "real_estates[0][zipcode]").send_keys("02723")
    self.driver.find_element(By.NAME, "real_estates[0][property_value]").send_keys("685999")
    self.driver.find_element(By.NAME, "real_estates[0][monthly_insurance]").send_keys("1414")
    Select(self.driver.find_element(By.NAME, "real_estates[0][property_type]")).select_by_value('SFR')
    Select(self.driver.find_element(By.NAME, "real_estates[0][status]")).select_by_value('RETAINED')
    Select(self.driver.find_element(By.NAME, "real_estates[0][occupancy]")).select_by_value('PR')
    Select(self.driver.find_element(By.NAME, "real_estates[0][intended_occupancy]")).select_by_value('PR')

    self.driver.find_element(By.ID, "add_mortgage_0").click()
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][creditor_name]").send_keys('Callable Mortgage')
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][account_number]").send_keys('987411547')
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][monthly_mortgage_payment]").send_keys('1671')
    self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][unpaid_balance]").send_keys('210027')
    Select(self.driver.find_element(By.NAME, "real_estates[0][mortgages][0][type]")).select_by_value('CONVENTIONAL')
    self.driver.find_element(By.ID, "add_additional_property").click()

    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "real_estates[1][street]")))
    self.driver.find_element(By.NAME, "real_estates[1][street]").send_keys("1234 Main Street")
    self.driver.find_element(By.NAME, "real_estates[1][city]").send_keys("Fairfax")
    self.driver.find_element(By.NAME, "real_estates[1][state]").send_keys("VA")
    self.driver.find_element(By.NAME, "real_estates[1][zipcode]").send_keys("22035")
    self.driver.find_element(By.NAME, "real_estates[1][property_value]").send_keys("423000")
    self.driver.find_element(By.NAME, "real_estates[1][monthly_insurance]").send_keys("608")
    Select(self.driver.find_element(By.NAME, "real_estates[1][property_type]")).select_by_value('SFR')
    Select(self.driver.find_element(By.NAME, "real_estates[1][status]")).select_by_value('RETAINED')
    Select(self.driver.find_element(By.NAME, "real_estates[1][occupancy]")).select_by_value('SH')
    Select(self.driver.find_element(By.NAME, "real_estates[1][intended_occupancy]")).select_by_value('IP')
    
    self.driver.find_element(By.ID, "add_mortgage_1").click()
    self.driver.find_element(By.NAME, "real_estates[1][mortgages][0][creditor_name]").send_keys('Best Ever Mtg')
    self.driver.find_element(By.NAME, "real_estates[1][mortgages][0][account_number]").send_keys('987411547')
    self.driver.find_element(By.NAME, "real_estates[1][mortgages][0][monthly_mortgage_payment]").send_keys('1671')
    self.driver.find_element(By.NAME, "real_estates[1][mortgages][0][unpaid_balance]").send_keys('210027')
    Select(self.driver.find_element(By.NAME, "real_estates[1][mortgages][0][type]")).select_by_value('CONVENTIONAL')

    
    self.driver.find_element(By.ID, "kyc_next_button").click()

###################################
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
    Select(self.driver.find_element(By.NAME, "property_address[your_asset]")).select_by_index(2)
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

  

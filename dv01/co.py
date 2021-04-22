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
    self.driver.find_element(By.ID, "email").send_keys("comarydv01@mail.com")
    self.driver.find_element(By.ID, "password").send_keys("Mary1234=")
    self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[1]/form/div[3]/div[3]/button").click()
######################################

    # Start KYC
    kyctrigger = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li.w-1\/4:nth-child(4) > a:nth-child(1) > div:nth-child(2)")))
    kyctrigger.click()
    joint = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div/a/div")))
    joint.click()


####################################
#     # Step 01 Full name
#     self.driver.implicitly_wait(5) # seconds
#     name = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[first_name]")))
#     name.send_keys("Mary")
#     self.driver.find_element(By.NAME, "kyc[last_name]").send_keys("Freddie")
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 02 Birth Date
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][0]")).select_by_value('MARCH')
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][1]")).select_by_value('30')
#     Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][2]")).select_by_value('1965')
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
#     #####################################

#     # Step 06 Marital Status
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[marital_status]")))
#     Select(self.driver.find_element(By.NAME, "kyc[marital_status]")).select_by_value('MARRIED')
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 07 SSN
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "ssn_number")))
#     ssn = self.driver.find_element(By.ID, "ssn_number")
    
#     if ssn.get_attribute('value') == None:
#         ssn.send_keys("990-20-0002")
#     else:
#         ssn.clear()
#         ssn.send_keys("990-20-0002")

#     self.driver.find_element(By.CSS_SELECTOR, ".fa-2x").click()
#     self.driver.find_element(By.ID, "kyc_step7_next_button").click()
# #####################################

#     # Step 08 Phone Number
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[home_phone_number]")))

#     home_phone = self.driver.find_element(By.NAME, "kyc[home_phone_number]")
#     if home_phone.get_attribute('value') == None:
#         home_phone.send_keys("(202) 222-2222")
#     else:
#         home_phone.clear()
#         home_phone.send_keys("(202) 222-2222")

#     cell_phone = self.driver.find_element(By.NAME, "kyc[cell_phone_number]")
#     if cell_phone.get_attribute('value') == None:
#         cell_phone.send_keys("(202) 666-6666")
#     else:
#         cell_phone.clear()
#         cell_phone.send_keys("(202) 666-6666")

#     work_phone = self.driver.find_element(By.NAME, "kyc[work_phone_number]")#Work
#     if work_phone.get_attribute('value') == None:
#         work_phone.send_keys("(202) 888-8888") 
#     else:
#         work_phone.clear()
#         work_phone.send_keys("(202) 888-8888") 


#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 09 Current Address
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "current_address[street]")))
#     # self.driver.find_element(By.NAME, "current_address[street]").click()
#     self.driver.find_element(By.NAME, "current_address[street]").send_keys("175 13th Street")
#     # self.driver.find_element(By.NAME, "current_address[city]").click()
#     self.driver.find_element(By.NAME, "current_address[city]").send_keys("Washington")
#     # self.driver.find_element(By.NAME, "current_address[zipcode]").click()
#     self.driver.find_element(By.NAME, "current_address[zipcode]").send_keys("20013")
#     # self.driver.find_element(By.NAME, "current_address[years]").click()
#     Select(self.driver.find_element(By.NAME, "current_address[years]")).select_by_value('16')
#     Select(self.driver.find_element(By.NAME, "current_address[months]")).select_by_value('4')
#     Select(self.driver.find_element(By.NAME, "current_address[housing]")).select_by_value('OWN')
#     # self.driver.find_element(By.NAME, "current_address[rent_per_month]").click()
#     self.driver.find_element(By.NAME, "current_address[rent_per_month]").send_keys("1950")
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# ####################################

#     # Step 10 Mailing Address
#     check = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/label/input[2]")))
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
#     self.driver.find_element(By.NAME, "current_employments[0][employer_name]").send_keys("US Navy")
#     # self.driver.find_element(By.NAME, "current_employments[0][position]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][position]").send_keys("Lieutenant")
#     # self.driver.find_element(By.NAME, "current_employments[0][phone]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][phone]").send_keys("3334445555")
#     # self.driver.find_element(By.NAME, "current_employments[0][street]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][street]").send_keys("2400 US Army Dr.")
#     # self.driver.find_element(By.NAME, "current_employments[0][city]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][city]").send_keys("Someplace")
#     # self.driver.find_element(By.NAME, "current_employments[0][state]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][state]").send_keys("MA")
#     # self.driver.find_element(By.NAME, "current_employments[0][zipcode]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][zipcode]").send_keys("02723")
#     # self.driver.find_element(By.NAME, "current_employments[0][start_date][0]").click()
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][0]")).select_by_value('SEPTEMBER')
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][1]")).select_by_value('1')
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][2]")).select_by_value('1999')
#     # self.driver.find_element(By.NAME, "current_employments[0][base_income]").click()

#     self.driver.find_element(By.ID, "add_current_employment_income_0").click()
#     self.driver.find_element(By.NAME, "current_employments[0][base_income]").send_keys("7680")
#     self.driver.find_element(By.NAME, "current_employments[0][military_entitlements]").send_keys("776")
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

    # Step 16 Tell us about your assets.
    self.driver.implicitly_wait(10) # seconds
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_joint_asset_true")))
    self.driver.find_element(By.ID, "kyc_joint_asset_true").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

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
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .pt-6:nth-child(3) > .trueblok-radio").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .pt-6:nth-child(4) .trueblok-checkmark").click()
    self.driver.find_element(By.CSS_SELECTOR, ".pt-6:nth-child(6) .trueblok-checkmark").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

  

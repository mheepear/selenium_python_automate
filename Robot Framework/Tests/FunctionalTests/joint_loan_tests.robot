*** Settings ***
Documentation  KYC Joint Loan
Library  SeleniumLibrary
Library  FakerLibrary
Resource  ../../Resources/PageObjects/Login.robot
Resource  ../../Resources/PageObjects/Dashhandler.robot
*** Variables ***
${URL}  http://portal.dev.getzense.com
${BROWSER}  Firefox


*** Test Cases ***
Verify the login into the GetZense account
    [documentation]  Enter a valid email address and valid password
    [tags]  Functional

    Login.Start Test Case
    Login.Verify Test Case


Borrower start to begin KYC
    [documentation]   Borrower click wether to continue or start
    [tags]  Functional

    Dashhandler.Continue KYC


Main borrower applies for a purchase individually.
    [documentation]   Main borrower selects purchase, then individual loan
    [tags]  Functional

    kyc.Type of Loan
    kyc.Type of Credit
    kyc.Type Confirmation


Once the user has choosed a type of application they should provide their name.
    [documentation]   Main borrower input their name in
    [tags]  Functional

    sleep  1
    wait until element is visible  name = kyc[first_name]
    wait until element is visible  name = kyc[middle_name]
    wait until element is visible  name = kyc[last_name]
    ${fname} =  FakerLibrary.FirstName
    ${lname} =  FakerLibrary.LastName
    input text  name= kyc[first_name]  ${fname}
    input text  name= kyc[last_name]  ${lname}
    click button  id= kyc_next_button

Provide Birth Date
    [documentation]   Main borrower input their birth date in
    [tags]  Functional

    sleep  1
    ${month}  Select random month
    select from list by value  name= kyc[date_of_birth][0]  ${month}
    ${day}  Select random day
    select from list by value  name=kyc[date_of_birth][1]  ${day}
    ${year} =  Select random year
    select from list by index  name=kyc[date_of_birth][2]  ${year}
    click button  //*[@id="kyc_next_button"]

Provide Gender
    [documentation]   Main borrower input their gender
    [tags]  Functional

    sleep  1
    wait until element is visible  name = kyc[gender]
    ${gender}  Select random gender
    click element  name = kyc[gender]
    select from list by index  name = kyc[gender]  ${gender}
    click element  //*[@id="kyc_next_button"]

Provide Dependent
    [documentation]   Main borrower input their dependent
    [tags]  Functional

    sleep  1
    select from list by index  name = kyc[dependents_number]  0

    ...  ElSE IF  ${dependent} == 2  for  ${i}  in  ${dependent}
    ...                              input text  name = kyc[dependents_ages][${i}]  ${number}
    ...                              END
    ...  ElSE IF  ${dependent} == 4  select from list by value  name = kyc[dependents_ages][0]  ${number}
    ...  ElSE IF  ${dependent} == 4  select from list by value  name = kyc[dependents_ages][0]  ${number}
    ...  ElSE IF  ${dependent} == 5  select from list by value  name = kyc[dependents_ages][0]  ${number}
    ...  ElSE IF  ${dependent} == 6  select from list by value  name = kyc[dependents_ages][0]  ${number}
    ...  ElSE  ${dependent} == 7+  select from list by value  name = kyc[dependents_ages][0]  ${number}

    click button  //*[@id="kyc_next_button"]

Provide Citizenship
    [documentation]   Main borrower input their gender
    [tags]  Functional

    wait until element is visible  name = kyc[citizenship]
    ${citizen}  select random citizen
    select from list by index  name = kyc[citizenship]  ${citizen}
    click button  //*[@id="kyc_next_button"]

Provide Marital Status

    wait until element is visible  name = kyc[marital_status]
    ${marital}  select random marital
    select from list by index  name = kyc[marital_status]  ${marital}
    click button  //*[@id="kyc_next_button"]

Provide SSN
    wait until element is visible  name = ssn_number
    ${ssn} =  FakerLibrary.Invalid Ssn
    input text  name = ssn_number  ${ssn}
    click button  //*[@id="kyc_step7_next_button"]

Provide phone number

    wait until element is visible  name = kyc[home_phone_number]
    ${phone} =  FakerLibrary.Phone Number
    ${phone2} =  FakerLibrary.Phone Number
    ${phone3} =  FakerLibrary.Phone Number

    input text  name = kyc[home_phone_number]  ${phone}
    input text  name = kyc[cell_phone_number]  ${phone3}
    input text  name = kyc[work_phone_number]  ${phone2}
    click button  //*[@id="kyc_next_button"]

Provide address

    click button  //*[@id="kyc_next_button"]

Provide current address
    click button  //*[@id="kyc_next_button"]
*** Keywords ***


Click KYC
    wait until element is visible  link = Fill it now
    press keys  link = Fill it now  [RETURN]

Continue KYC
    wait until element is enabled  link = Continue filling
    press keys  link = Continue filling  [RETURN]

Continue check
    ${result}=  Run keyword and ignore error  Element should be visible  ${node A}
    Run keyword if  '${result[0]}' == 'PASS'
    ...  press keys  ${node A}  [RETURN]
    ...  ELSE
    ...  press keys  ${node B}  [RETURN]

Select random month
    ${randomValue}  Random Element  ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    [Return]  ${randomValue}

Select random day
    ${randomValue}  Random Element  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    [Return]  ${randomValue}

Select random year
    ${randomValue}  Random Element  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    [Return]  ${randomValue}

Select random gender
    ${randomValue}  Random Element  ['0', '1', '2']
    [Return]  ${randomValue}

Select random dependent
    ${randomValue}  Random Element  ['2']
    [Return]  ${randomValue}

Select random citizen
    ${randomValue}  Random Element  ['0', '1', '2']
    [Return]  ${randomValue}

Select random marital
    ${randomValue}  Random Element  ['0', '1', '2']
    [Return]  ${randomValue}

*** Settings ***
Documentation  KYC Joint Loan
Library  SeleniumLibrary
Library  FakerLibrary

*** Variables ***
${URL}  https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit
${BROWSER}  Firefox
${node A}  link = Fill it now
${node B}  link = Continue filling

*** Test Cases ***
Verify the login into the GetZense account
    [documentation]  Enter a valid email address and valid password
    [tags]  Functional

Once the user has choosed a type of application they should provide their name.
    [documentation]   Main borrower input their name in
    [tags]  Functional

    wait until element is visible  name = kyc[first_name]
    ${fname}=  FakerLibrary.FirstName
    input text  id = fname  ${fname}
    ${lname}=  FakerLibrary.LastName
    input text  name = lname  ${lname}


*** Keywords ***
Start Test Case
    open browser  ${URL}  ${BROWSER}
    wait until element is visible  id = app
    click element  //*[@id="app"]/header/nav/ul/li[7]/a

Verify Test Case
    wait until element is visible  id = email
    input text  //*[@id="email"]  mhee@mail.com
    input password  //*[@id="password"]  Mhee1234=
    submit form

Click KYC
    ${newkyc}=  wait until element is visible  link = Fill it now
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
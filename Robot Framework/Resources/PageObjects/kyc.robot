*** Settings ***
Documentation    Loggin in
Library  SeleniumLinrary

*** Variables ***
${URL}  http://portal.dev.getzense.com
${BROWSER}  Firefox

*** Keywords ***
Type of Loan
    wait until element is visible  //*[@id="loan_purpose_purchase_button"]
    click element  //*[@id="loan_purpose_purchase_button"]
    sleep  1
Type of Credit
    wait until element is visible  //*[@id="type_of_credit_individual_button"]
    click element  //*[@id="type_of_credit_individual_button"]
Type Confirmation
    wait until element is visible  id = continue_button
    click button  id = continue_button
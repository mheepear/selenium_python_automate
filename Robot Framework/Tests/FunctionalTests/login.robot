*** Settings ***
Documentation  A resource file with reusable keywords and variables.
...
...  The system specific keywords created here form our own
...  domain specific language. They utilize keywords provided
...  by the imported SeleniumLibrary.
Library  SeleniumLibrary

*** Variables ***
${SERVER}  http://portal.dev.getzense.com
${BROWSER}  Firefox
${VALID USER}  mhee@mail.com
${VALID PASSWORD}  Mhee1234=
${LOGIN URL}  ${SERVER}/login
${WELCOME URL}  ${SERVER}/dashboard
${ERROR URL}  ${SERVER}/error.html


*** Test Cases ***
Verify Login
    [documentation]  Login with Valid Credentials
    [tags]  Functional
    Open Browser To Login Page
    Input Username  ${username}
    Input Password  ${password}
    Submit Credentials
    Welcome Page Should Be Open

*** Keywords ***
Open Browser To Login Page
    open browser  ${LOGIN URL}  ${BROWSER}
    maximize browser window
    Login Page Should Be Open

Login Page Should Be Open
    Title Should Be  zenze

Go To Login Page
    go to  ${LOGIN URL}
    Login Page Should Be Open

Input Username
    [Arguments]  ${username}
    input text  //*[@id="email"]  mhee@mail.com

Input Password
    [Arguments]  ${password}
    input password  //*[@id="password"]  Mhee1234=

Submit Credentials
    submit form

Welcome Page Should Be Open
    location should be  ${WELCOME URL}
    title should be  zense

Close Browser
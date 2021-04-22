
*** Settings ***
Documentation  A test suite with a single test for valid login.
Library  SeleniumLibrary

*** Variables ***
${URL}  http://portal.dev.getzense.com
${BROWSER}  Firefox

*** Test Cases ***
Verify the login into the GetZense account
    [documentation]  Main borrower selects purchase, then individual loan
    [tags]  Functional
    open browser  ${URL}  ${BROWSER}
    click element  //*[@id="app"]/header/nav/ul/li[7]/a
    input text  //*[@id="email"]  mhee@mail.com
    input password  //*[@id="password"]  Mhee1234=
    submit form

*** Keywords ***

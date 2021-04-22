*** Settings ***
Documentation    Loggin in
Library  SeleniumLinrary

*** Variables ***
${URL}  http://portal.dev.getzense.com
${BROWSER}  Firefox

*** Keywords ***
Start Test Case
    open browser  ${URL}  ${BROWSER}
    sleep  3
    wait until element is visible  link = Log in
    click element  link = Log in

Verify Test Case
    sleep  3
    wait until element is visible  id = email
    input text  //*[@id="email"]  mhee@mail.com
    input password  //*[@id="password"]  Mhee1234=
    submit form
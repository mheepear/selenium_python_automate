*** Settings ***
Documentation    Loggin in
Library  SeleniumLinrary

*** Variables ***
${URL}  http://portal.dev.getzense.com
${BROWSER}  Firefox

*** Keywords ***
Continue KYC
    wait until element is enabled  link = Continue filling
    press keys  link = Continue filling  [RETURN]
    sleep  1

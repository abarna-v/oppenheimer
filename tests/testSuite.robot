*** Settings ***
Library           String
Library           Process
Library           DateTime
Library           Collections
Library           OperatingSystem
Library           SeleniumLibrary

Library           ../libs/API/SendAPI.py
Library           ../libs/WEB/webPage.py

Variables         ./API.yaml

Suite Setup       configure_setup
Suite Teardown    cleanup_setup

*** Variables ***
${WAIT_TIME}      5s

*** Test Cases ***
TC_1: INSERT SINGLE PERSON RECORD
    [Documentation]        INSERT SINGLE RECORD OF A WORKING CLASS HERO
    [Tags]                 SingleRecord
    [Setup]                Check Oppenheimer Project
    ${POST_RESPONSE} =     Send API        POST    /calculator/insert              ${REQUESTDATA.insert_single_1}
    Log                    VERIFYING THE POSTED API DATA HAS BEEN REGISTERED
    ${GET_RESPONSE} =      Send API        GET     /calculator/taxRelief
    Log                    ${GET_RESPONSE}
    ${natid_value} =       JsonValuefromKey        ${REQUESTDATA.insert_single_1}    natid
    Log                    ${natid_value}
    Should Contain         ${REQUESTDATA.insert_single_1["natid"]}        ${natid_value}

TC_2: INSERT MULTIPLE PERSON RECORD
    [Documentation]        INSERT SINGLE RECORD OF A WORKING CLASS HERO
    [Tags]                 MultipleRecord
    [Setup]                Check Oppenheimer Project
    ${RESPONSE} =          Send API        POST    /calculator/insertMultiple      ${REQUESTDATA.insert_multiple.records}
    Log                    ${RESPONSE}
    Log                    JAR FILE THROWS AN ERROR FOR MULTIPLE RECORDS

TC_3: UPLOAD CSV FILE TO PORTAL
    [Documentation]        INSERT SINGLE RECORD OF A WORKING CLASS HERO
    [Tags]                 UploadCSV
    [Setup]                Check Oppenheimer Project
    ${CSV_PATH} =          Create CSV Data    ${EXECDIR}/utils/   ${REQUESTDATA.excel_datas}[records]
    ${DRIVER} =            Open Browser URL   ${BROWSER}          ${browserPath}     ${WEBPAGE.URL}
    Upload CSV Refresh Table   ${DRIVER}      ${CSV_PATH}
    Log                    VERIFYING THE UPLOADED DATA VIA API
    ${RESPONSE} =          Send API        GET     /calculator/taxRelief
    ${TAXRELIEF_VALUE} =   Compute Tax Relief      ${REQUESTDATA.excel_datas}[records][0]
    ${RESPONSE} =          Validate Tax Relief     ${RESPONSE}     ${REQUESTDATA.excel_datas}[records][0]    ${TAXRELIEF_VALUE}

TC_4: CALCULATE AMOUNT OF TAX RELIEF
    [Documentation]        CALCULATE TAX RELIEF FOR A GIVEN RECORD
    [Tags]                 TaxRelief
    [Setup]                Check Oppenheimer Project
    ${TAXRELIEF_VALUE} =   Compute Tax Relief      ${REQUESTDATA.insert_single_2}
    Log                    VERIFYING THE TAX RELIEF DATA VIA API
    ${RESPONSE} =          Send API        GET     /calculator/taxRelief
    ${RESPONSE} =          Validate Tax Relief    ${RESPONSE}     ${REQUESTDATA.insert_single_2}    ${TAXRELIEF_VALUE}

TC_5: DISPENSE TAX RELIEF TO WORKING CLASS HEROES
    [Documentation]        DISPENSE THE TOTAL TAX RELIEF RECORDS TO ALL HEROES
    [Tags]                 DispenseCash
    [Setup]                Check Oppenheimer Project
    ${DRIVER} =            Open Browser URL       ${BROWSER}         ${browserPath}     ${WEBPAGE.URL}
    ${DRIVER} =            Dispense Tax Relief    ${DRIVER}

*** Keywords ***
configure_setup
    [Documentation]        Initializing Oppenheimer Project !!!
    ${curr_system} =       Evaluate           platform.system()    platform
    ${jarPath} =           Set Variable If    '${curr_system}' == 'Darwin'    ${EXECDIR}/utils/oppenheimer-project-dev/OppenheimerProjectDev.jar
    Set Global Variable    ${jarPath}
    ${browserPath} =       Set Variable If    '${curr_system}' == 'Darwin'    ${EXECDIR}/utils/${BROWSER}driver    ${EXECDIR}/utils/${BROWSER}driver.exe
    Set Global Variable    ${browserPath}
    Execute Oppenheimer Project
    ${JAR_PID} =           Get JAR ProcessID

Check Oppenheimer Project
    ${JAR_PID} =           Get JAR ProcessID    
    Run Keyword If         '''${JAR_PID[2]}''' == '1'    Restart Oppenheimer Project

Execute Oppenheimer Project
    ${JAVA_JAR} =          Set Variable           nohup java -jar ${jarPath} &
    Set Global Variable    ${JAVA_JAR}
    ${RESULT} =            Execute JAR Project    ${JAVA_JAR}

Get JAR ProcessID
    ${OUTPUT} =            Execute Command        ${PROCESS.GET_PID}
    Log                    Executed Process ID : ${OUTPUT[0]}
    #${JAR_PROCESSID} =     Set Global Variable    ${OUTPUT[0]}
    Run Keyword If         '''${OUTPUT[2]}''' == '0'    Log        Oppenheimer Project JAR is Running !!
    [Return]               ${OUTPUT[0]}

Kill JAR Process
    [Arguments]            ${PROCESS_ID}
    ${OUTPUT} =            Execute Command        kill -9 ${PROCESS_ID}
    Log to Console         ${OUTPUT[0]}
    Run Keyword If         '''${OUTPUT[2]}''' == '0'    Log        Successfully killed Oppenheimer JAR Process !!!

Restart Oppenheimer Project
    ${jar_process_id} =    Get JAR ProcessID
    Kill JAR Process       ${jar_process_id}
    Execute Oppenheimer Project
    
cleanup_setup
    [Documentation]        Cleaning the Suite Setup
    Log to Console         Cleaning the Oppenheimer Project !!!
    Close All Browsers
    ${jar_process_id} =    Get JAR ProcessID
    Kill JAR Process       ${jar_process_id}



import os
import sys
import time

from SeleniumLibrary import SeleniumLibrary

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from Elements import *

try:
    from robot.api import logger
except ImportError:
    import logging
    logger = logging.getLogger(__name__)
    LOG_HNDLR = logging.StreamHandler(sys.stdout)
    LOG_HNDLR.setFormatter(logging.Formatter('%(asctime)-6s\t[%(levelname)-5s]\t[%(module)s.%(funcName)\s:%(lineno)-3d]\t   %(message)s'))
    LOG_HNDLR.setLevel(logging.DEBUG)
    logger.addHandler(LOG_HNDLR)
    logger.setLevel(logging.DEBUG)

# pylint: disable=locally-disabled, invalid-name
# pylint: disable=too-many-ancestors

__author__ = "Abarna Ravi"
__version__ = "1.0.0"
__email__ = "abarnaravi6@gmail.com"
__status__ = "UI Automation Framework"


###############################################
###    UI functionality of the Website      ###
###############################################
class webPage():
    
    def __init__(self):
        """
        Initializing all the class definitions
        """
        pass
    
    @keyword(name='Open Browser URL')
    def open_browser_url(self, browser, browser_path, url):
        """
        When user sends the args as browser, browser_path and URL
    
        Parameters:
        driver : Selenium webdriver(browser)
        browser (str): Type of Browser (chrome or firefox)
        browser_path (int): Browser path exists 
        url (str): URL to Open
    
        Returns: webdriver
        """
        logger.debug("Browser Path : ", browser_path)
        if browser.lower() == "chrome":
            logger.debug("Proceeding with Chrome browser !!!")
            driver = webdriver.Chrome(browser_path)
        elif browser.lower() == "firefox":
            logger.debug("Proceeding with Firefox browser !!!")
            driver = webdriver.Firefox(browser_path)
        else:
            logger.error("Given browser is not supported. Proceeding with Chrome Browser !!!")
            # browser = get_default_browser_name()
            driver = webdriver.Chrome(browser_path)
        # # Loading the given URL
        driver.get(url)
        time.sleep(5)
        driver.maximize_window()
        driver.implicitly_wait(25)
        logger.debug(driver.title)
        return driver
        # assert browser_title in driver.title

    @keyword(name='Upload CSV Refresh Table')
    def upload_csv_refresh_table(self, driver, filepath):
        """
        Uploading the given CSV file using browse options
        Refresh the table and verify the values are loaded 
        
        Parameters:
        driver : Selenium webdriver(browser)
        filepath (str): Upload filepath
    
        Returns: webdriver , status_of_upload
        """
        try:
            ## verifying the browse icon to upload
            elem = driver.find_element_by_xpath(browse_upload_file)         
            if elem:
                logger.debug("Uploading the file using Browse Options : {}".format(filepath))
                elem.send_keys(str(filepath))
                time.sleep(10)
                logger.info("Successfully uploaded the given file !")
            
            ## Refreshing the table after upload
            elem = driver.find_element_by_xpath(refresh_taxRelief_table).click()
            time.sleep(5)
            elem = driver.find_element_by_xpath(table_header_xpath)
            if elem:
                logger.debug("Refreshed the Tax Relief Table !!!")
                time.sleep(5)

        except Exception as Exp:
            logger.error("ERROR : Couldn't able to search !!!")
            raise Exp
        return driver
    
    @keyword(name='Dispense Tax Relief')
    def dispense_tax_relief(self, driver):
        """
        Dispensing the Total Tax Relief using Button Options
        
        Parameters:
        driver : Selenium webdriver(browser)
    
        Returns: webdriver , status_of_dispensed
        """
        try:
            ## verifying the browse icon to upload
            elem = driver.find_element_by_xpath(dispense_now_icon)         
            if elem:
                elem.click()
                logger.debug("Dispensing the Tax Relief !!")
                time.sleep(5)
            
            logger.debug("Verifying the Dispensed Tax Relief !!")
            elem = driver.find_element_by_xpath(cash_dispensed)
            if elem:
                logger.info("Successfully Dispensed the Cash !!")
                time.sleep(5)

        except Exception as Exp:
            logger.error("ERROR : Couldn't able to search !!!")
            raise Exp

        return driver

    @keyword(name='Close the Browsers')
    def close_the_browsers(self, driver):
        """
        Closing all the existing Browsers
        
        Parameters:
        driver : Selenium webdriver(browser)
            
        Returns: None
        """
        try:
            if driver:
                driver.close()
                logger.info("Closing the Browsers !!!")
        except Exception as Exp:
            logger.error("Couldn't able to Close Browsers !!!")
            raise Exp


# Testing Main Functions ###
if __name__ == '__main__':
    print ("Executing Main ...")
    # driver = obj.open_browser_url(browser, browser_path, url)
    print ("Completed Scripts !!!")


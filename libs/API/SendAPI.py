import os, os.path
import sys
import yaml
import json
import time
import requests
import subprocess
import pandas as pd

from datetime import datetime, date
from robot.api.deco import keyword

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


hdr = {
    'content-type': 'application/json',
#    'Accept-Charset': 'UTF-8',
    'Accept-Encoding': None
}

# pylint: disable=locally-disabled, invalid-name
# pylint: disable=too-many-ancestors

__author__ = "Abarna Ravi"
__version__ = "1.0.0"
__email__ = "abarnaravi6@gmail.com"
__status__ = "UI Automation Framework"


###############################################
###    API functionality of the Website     ###
###############################################

@keyword ("Execute JAR Project")
def execute_jar_project(command):
    '''
    Executing command with Popen
    '''
    logger.info ("Creating the Oppenheimer Project ...")
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = p.stderr.read(1)
        logger.debug("Execution Output : {}".format(output))
        if output == '' and p.poll() != None:
            logger.error("Process is not started properly !!!")
            return -1
        if output != '':
            sys.stdout.write(output)
            sys.stdout.flush()
            time.sleep(5)
            logger.debug("Waiting for the Oppenheimer Project to get started ...")
            time.sleep(30)
            logger.info ("Executed the Oppenheimer Project Jar Successfully !!!")
            return 0
        
@keyword ("Execute Command")
def execute_command(command):
    try:
        logger.debug("Executing the given command {}".format(command))
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        logger.info("Executed Output : {}".format(stdout))
        if proc.returncode == 0:
            return (stdout, stderr, proc.returncode)
        else:
            logger.error("Command couldn't Execute : {}".format(stdout))
            return -1
    except Exception as Exp:
        logger.error(Exp)

@keyword ("Send API")
def send_API(method, apiurl, requestdata='None'):
    '''
    Defining the API Request with Arguments
    '''
    api_url_base = 'http://' + "localhost:8080"
    requesturl = api_url_base + apiurl
    logger.debug("Requesting URL : {}".format(requesturl))
    
    payload = json.dumps(requestdata)
    logger.debug("Request Data : {}".format(payload))
    output = "Empty"
    
    try:
        if method.lower() == "post":
            response = requests.post(url=requesturl, data=payload, headers=hdr)
        elif method.lower() == "get":
            response = requests.get(url=requesturl, data=payload, headers=hdr)
        elif method.lower() == "put":
            response = requests.put(url=requesturl, data=payload, headers=hdr)
        elif method.lower() == "delete":
            response = requests.delete(url=requesturl, data=payload, headers=hdr)
        time.sleep(2)
        logger.debug("Response : {}".format(response))
        
        if response.text:
            logger.debug("Response Text : {}".format(response.text))
            output = format(response.text)
            # output = json.loads(response.text)
            # logger.debug("Response Output : {}".format(output))
        else:
            logger.error("Response Output is Empty {} !! ".format(response.text))

    # Code here will only run if the request is successful
    except requests.exceptions.HTTPError as errh:
        logger.error(errh)
    except requests.exceptions.ConnectionError as errc:
        logger.error(errc)
    except requests.exceptions.Timeout as errt:
        logger.error(errt)
    except requests.exceptions.RequestException as err:
        logger.error(err)
    except Exception as Exp:
        logger.error(Exp)

    return output


@keyword ("Compute Tax Relief")
def compute_tax_relief(record_dict):
    '''
    Compute Tax Relief for Single Person Records
    '''
    tax_relief = 0
    single_record_dict = {}
    
    try:
        # for k,v in kwargs.items():
        #     single_record_dict = kwargs[k]
        single_record_dict = record_dict
        logger.debug("Given Single Record Dict : {}".format(single_record_dict))
        
        for key in single_record_dict:            
            if key == 'salary':
                salary = single_record_dict[key]
            if key == 'gender':
                gender = single_record_dict[key]
            if key == 'tax':
                tax_paid = single_record_dict[key]
            if key == 'birthday':
                birthday = single_record_dict[key]

        logger.debug ("Salary : {}, Tax Paid : {} ".format(salary,tax_paid))
    
        ## Changing birthday into DOB format
        if birthday:
            born_date = str(birthday)[0:2]
            born_month = str(birthday)[2:4]
            born_year = str(birthday)[4:8] 
            today = date.today()
            age = today.year - int(born_year) - ((today.month, today.day) < (int(born_month), int(born_date)))
            logger.debug ("AGE : {}".format(age))

        if age:
            variable = 0
            #import pdb;pdb.set_trace()
            if 19 <= age <= 35:
                variable = 0.8
            elif 36 <= age <= 50:
                variable = 0.5
            elif 51 <= age == 75:
                variable = 0.367
            elif age >= 76:
                variable = 0.05
            elif age <= 18:
                variable = 1
                
        logger.debug ("variable : {}".format(variable))
        if variable == 0:
            raise Exception
        
        ## Calculating Tax Relief for Each person
        gender_bonus = 0
        if gender == 'F':
            gender_bonus = 500
        logger.debug ("gender_bonus : {}".format(gender_bonus))
        
        tax_relief = ((int(salary) - int(tax_paid)) * variable ) + int(gender_bonus)
        logger.debug ("tax_relief : {}".format(type(tax_relief)))
        formatted_tax_relief = "{:.2f}".format(tax_relief)
        logger.debug ("tax_relief : {}".format(formatted_tax_relief))

    except Exception as Exp:
        logger.error(Exp)
    
    return formatted_tax_relief

@keyword ("Create CSV Data")
def create_csv_data(filepath, record_lists):
    '''
    Sending the Multiple Record as List of Dictionaries
    Creating and adding the necessary Values in the Excel Sheet
    Returning the Path of the Excel File
    '''
    logger.debug("Given Records {}".format(record_lists))

    ## If key contains nested dictionary values
    newDict = {}
    newDict = ({key: [i[key] for i in record_lists] for key in record_lists[0]})
    logger.debug("")
    logger.debug("Given Records to add in Excel Sheet {}".format(newDict))


    ## Excel Path file from input args
    t = time.localtime()
    timestamp = time.strftime('%s', t)
    full_file_name = os.path.join(filepath, 'excel_records' + "_" + timestamp + '.csv')
    logger.debug ("Uplolading CSV File : {}".format(full_file_name))

    try:
        ### key contains nested dictionary values
        data_frame = pd.DataFrame(newDict).to_csv(full_file_name, header=True, index=False)
        if full_file_name:
            return full_file_name
    except Exception as Exp:
        raise (Exp)
        return -1


@keyword ("JsonValuefromKey")
def JsonValuefromKey(Original, givenKey):
    '''
    ### Get value from the given ID in single lists ###
    '''
    ndictID = {}
    returnValue = None
    logger.debug("Given Key to fetch value : '{}'".format(givenKey))
    try:
        #Original = ast.literal_eval(json.dumps(Original))
        Original = eval(str(Original))
        for IDKey, IDValue in Original.items():
            # logger.debug("IDKey : {}".format(IDKey))
            if IDKey == givenKey:
                ndictID[IDKey] = IDValue
                returnValue = IDValue
                break
    except Exception as Exp:
        logger.error(Exp)
        raise Exception
    logger.debug("Fetched Dictionary : {}".format(ndictID))
    logger.debug("Passing Dictionary Value : {}".format(returnValue))
    return returnValue


@keyword ("Validate Tax Relief")
def validate_tax_relief(api_json, input_single_json, taxRelief):
    '''
    Validating the Tax Relief from API JSON OUTPUT
    Verifying the value from the TaxRelief
    '''
    api_json = eval(str(api_json))
    input_single_json = eval(str(input_single_json))

    logger.debug("Given taxRelief : {}".format(taxRelief))
    natid_value = JsonValuefromKey(input_single_json, 'natid')
    name_value = JsonValuefromKey(input_single_json, 'name')
    logger.debug("TYPE OF natid_value : {}".format(type(natid_value)))
    logger.debug("TYPE OF name_value : {}".format(type(name_value)))
    logger.debug("The API Json Lists : {}".format(api_json))
    
    try:
        result = None
        for sub in api_json:
            if sub['natid'] == natid_value and sub['name'] == name_value:
                #logger.debug ("tax_relief : {}".format(type(sub['relief'])))
                if sub['relief'] == taxRelief:
                    logger.debug("TaxRelief Values are Matching with the API Response !!!")
                    break
    except Exception as Exp:
        logger.error(Exp)
    return 0

# if __name__ == "__main__":
#     print(response)
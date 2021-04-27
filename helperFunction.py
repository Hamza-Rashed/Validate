from xml.etree import ElementTree as ET
import json


def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

##############################################  For Json  ###############################################


def valodateJsonValue(jsonText):
    ''' Check if there any value from json Massege is illogical '''
    listIds = []
    data = json.loads(jsonText)
    for n in data['taxes']:
        listIds.append(n['id'])
        if type(n['name']) is not str:
            return 'Name must be str'
        elif type(n['applied_money']['amount']) is not int:
            return 'The amount must be int !! '
        elif type(n['rate']) is not float:
            return 'The rate must be float !! '
        elif type(n['is_custom_amount']) is not bool:
            return 'The is custom amount must be bool !! '

    result = checkIfDuplicates_1(listIds)
    if result:
        return 'OMG Man !! The Bill is Reapeted'
    return True


def validateJsonFormat(jsonText):
    ''' Check is Ensure that the formats are correct for the json massege '''
    try:
        json.loads(jsonText)
    except ValueError as err:
        return False
    return True


################################################  For XML ##################################################

def validateXMLValue(XMLText):
    ''' Check if there any value from XML Massege is illogical '''
    listIds = []
    data = ET.fromstring(XMLText)
    for n in data.findall('element'):
        idElement = n.find('id').text
        NameElement = n.find('name').text
        amountElement = int(n.find('applied_money').find('amount').text)
        rateElement = float(n.find('rate').text)
        currencyElement = n.find('applied_money').find('currency').text
        listIds.append(idElement)
        if type(currencyElement) is not str:
            return 'currency must be str'
        elif type(amountElement) is not int:
            return 'The amount must be int !! '
        elif type(rateElement) is not float:
            return 'The rate must be float !! '
        elif type(NameElement) is not str:
            return 'The name must be str !! '

    result = checkIfDuplicates_1(listIds)
    if result:
        return 'OMG Man !! The Bill is Reapeted'
    return True


def validateXMLFormat(XMLText):
    ''' Check is Ensure that the formats are correct for the XML massege '''
    try:
        ET.fromstring(XMLText)
    except ValueError as err:
        return False
    return True

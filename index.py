from xml.dom import minidom
from lxml import etree
import json

def validateJsonText(jsonText):
	""" Validate any json string For Ex : 
			jsonText =
		{
			"id" : "cfc92a12-f847-4942-b6ec-1454d194c9ba",
			"name" : "Sales Tax",
			"rate" : 0.16,
			"inclusion_type" : "INCLUSIVE",
			"is_custom_amount" : true,
			"applied_money" : {
				"amount" : 483,
				"currency" : "JOD"
			}
		}

	"""
	try:
		json.loads(jsonText)
	except ValueError as err:
		print(err)
		return False
	return True

	# try:
    #     json.load(jsonFile)
    # except ValueError as err:
    #     print(err)
    #     return False
    # return True

def validateJsonFile(jsonFile):
	""" Validate any json file but you need to open it then you have to put it as a param """
	try:
		json.load(jsonFile)
	except ValueError as err:
		print(err)
		return False
	return True

# with open("trans/transaction.json") as f:
#     print(validateJsonFile(f))

def validateXMLFile(XMLFile):
	""" Validate any XML File """
	if minidom.parse(XMLFile).toxml():
		return True
	return False

def validateXMLText(XMLText):
	""" Validate any XML String For Example : 
	data =
<root>
    <additive_tax_money>
        <amount>0</amount>
        <currency>JOD</currency>
    </additive_tax_money>
	    <business_id>3f522ee8-7e69-4d78-aeb5-5278aaf21558</business_id>
    <creation_time>2017-02-09T10:49:34.000Z</creation_time>
    <creator>
        <email>anonymous@example.com</email>
        <id>00000000-0000-0000-0000-000000000000</id>
        <name>John Doe</name>
    </creator>
</root>
	"""
	
	if minidom.parseString(data):
		return True
	return False
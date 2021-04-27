from index import Validate
from helperFunction import validateJsonFormat, valodateJsonValue, validateXMLFormat, validateXMLValue

# Lets take an example for the json massege and XML massege

jsonText = '''
{"taxes" : [ 
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
                },
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
            ]}
			'''

XMLText = '''
    <taxes>
        <element>
            <applied_money>
                <amount>483</amount>
                <currency>JOD</currency>
            </applied_money>
            <id>cfc92a12-f847-4942-b6ec-1454d194c9ba</id>
            <inclusion_type>INCLUSIVE</inclusion_type>
            <is_custom_amount>true</is_custom_amount>
            <name>Sales Tax</name>
            <rate>0.16</rate>
        </element>
        <element>
            <applied_money>
                <amount>483</amount>
                <currency>JOD</currency>
            </applied_money>
            <id>cfc92a12-f847-4942-b6ec-1454d194c9a</id>
            <inclusion_type>INCLUSIVE</inclusion_type>
            <is_custom_amount>true</is_custom_amount>
            <name>Sales Tax</name>
            <rate>0.16</rate>
        </element>
    </taxes>
'''


# Now lets apply our class and check the masseges
rootJson = Validate(jsonText, validateJsonFormat, valodateJsonValue)
resultJson = rootJson.validateMassege()
# print(resultJson)

rootXML = Validate(XMLText, validateXMLFormat, validateXMLValue)
resultXML = rootXML.validateMassege()
# print(resultXML)

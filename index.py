from xml.dom import minidom
from lxml import etree
import json


class Validate:
    def __init__(self, massegeText, formatType, checkValue):
        self.massegeText = massegeText
        self.formatType = formatType
        self.checkValue = checkValue


    def validateMassege(self):
        """ Validate any json string For Ex : """
        if self.formatType(self.massegeText) == True:
            if self.checkValue(self.massegeText) == True:
                return "all Thing is good"
            return self.checkValue(self.massegeText)
        return "Format Not Correct"


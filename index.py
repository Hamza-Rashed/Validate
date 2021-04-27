
class Validate:
    def __init__(self, massegeText, formatType, checkValue):
        self.massegeText = massegeText
        self.formatType = formatType
        self.checkValue = checkValue


    def validateMassege(self):
        """ Validate any json and XML massege """
        if self.formatType(self.massegeText) == True:
            if self.checkValue(self.massegeText) == True:
                return "all Thing is good"
            return self.checkValue(self.massegeText)
        return "Format Not Correct"


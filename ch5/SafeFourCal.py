import secrets
from ch5.MoreFourCal import MoreFourCal

class SafeFourCal(MoreFourCal):
    
    def divide(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second
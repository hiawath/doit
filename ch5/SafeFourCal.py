from .MoreFourCal import MoreFourCal

class SafeFourCal(MoreFourCal):
    
    def divide(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second
        
        
if __name__=="__main__":
    a=SafeFourCal(2,0)
    print(a.add())
    print(a.minus())
    print(a.mul())
    print(a.divide())
    print(a.pow())
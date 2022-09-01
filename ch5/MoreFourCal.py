from .FourCal import FourCal

class MoreFourCal(FourCal):
    def pow(self):
        result=self.first ** self.second
        return result
    
if __name__=="__main__":
    a=MoreFourCal(1,2)
    print(a.add())
    print(a.minus())
    print(a.mul())
    print(a.divide())
    print(a.pow())
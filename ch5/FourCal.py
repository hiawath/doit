
class FourCal:
    result=0
    
    def __init__(self, first=0,second=0):
        self.first=first
        self.second=second
       
    def setdata(self,first:int, second:int):
        self.first=first
        self.second=second

    def add(self):
        FourCal.result = self.first+self.second
        return FourCal.result
    def minus(self):         
        FourCal.result =self.first-self.second
        return FourCal.result
    
    def mul(self):
        FourCal.result =self.first*self.second
        return FourCal.result
    
    def divide(self):
        FourCal.result =self.first/self.second
        return FourCal.result


if __name__=="__main__":
    a=FourCal(1,2)
    print(a.add())
    print(a.minus())
    print(a.mul())
    print(a.divide())
    
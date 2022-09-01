from ch5.Calculator import Calculator as Cal
from ch5 import CountFromBy as CF
from ch5.MoreFourCal import MoreFourCal
from ch5.SafeFourCal import SafeFourCal

cal1=SafeFourCal(4,2)
cal2=MoreFourCal()
cal3=MoreFourCal(1)


#cal1.setdata(1,1)
#cal2.setdata(2,2)

print(cal1.add())
print(cal1.minus())
print(cal1.mul())
print(cal1.divide())
print(cal1.pow())



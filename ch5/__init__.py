# __init__.py
import types
#from ch5.MoreFourCal import MoreFourCal
#from .Calculator import Calculator
#from .CountFromBy import CountFromBy
#from .FourCal import FourCal
#from .MoreFourCal import MoreFourCal
#from .SafeFourCal import SafeFourCal

#__all__ = ['FourCal','MoreFourCal','SafeFourCal']
__all__ = [name for name, obj in globals().items()
           if not name.startswith('_') and not isinstance(obj, types.ModuleType)
           and name not in {'wantobjects'}]

a=1

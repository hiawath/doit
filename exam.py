    
def all4(iterable):
    for element in iterable:
        if not element:
            return False
    return True

all4([])
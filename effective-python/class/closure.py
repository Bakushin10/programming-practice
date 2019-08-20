def number():
    x = 100

    def add():
        print(x)
    
    return add()

def numberObject():
    x = 100

    def add():
        print(x)
    
    return add


a = number()
b = numberObject()
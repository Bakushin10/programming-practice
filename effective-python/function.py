
# bad
def devide_bad(a,b):
    try:
        return a /b
    except ZeroDivisionError:
        return None

def divede_better(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs")

def divede_better2(a, b):
    x, y = 5, 2
    try:
        result = x /y
    except ValueError:
        print("invalid inputs")
    else:
        print("result is {}".format(result))

# x, y = 0, 5
# result = divede_better(x, y)
# if result is None:
#     print("invalid inputs")


"""
item 15

closure
"""
def sort_priority(values, group):
    def helper(x):
        if x in group:
            print(x)
            return (0, x)
        return (1,x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


"""
item 19
"""

def remainder(number, divisor):
    return number % divisor

print(remainder(20,7))
print(remainder(number = 20, divisor = 7))
print(remainder(divisor = 7, number = 20))


"""
item 20
"""
from datetime import datetime
def log(message, when = None):
    """
    Log a message with a timestamp.
        
    Args:
        message: Message to print.
        when: datetime of when the message occurred.
        Defaults to the present time.
    """
    when = datetime.now() if when is None else when
    print("{}: {}".format(when, message))

log("Hi there!")



"""
Default arguments are only evaluated once: during function definition at module
load time. This can cause odd behaviors for dynamic values (like {} or []).


Use None as the default value for keyword arguments that have a dynamic value.
Document the actual default behavior in the function's docstring.
"""


import json
def decodeBad(data, default={}):
    """
    cause an data inconsistancy
    """
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decodeBad("bad data")
foo["stuff"] = 5
bar = decodeBad("also bad")
bar["meep"] = 1
print("Foo:", foo)
print("Bar:", bar)


def decodeBetter(data, default=None):
    """
    
    """

    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decodeBetter("bad data")
foo["stuff"] = 5
bar = decodeBetter("also bad")
bar["meep"] = 1
print("Foo:", foo)
print("Bar:", bar)


def getListBad(data, default=[]):
    if data == 1:
        return data
    else:
        return default

def getListBetter(data, default=None):
    if default is None:
        default = []
    if data == 1:
        return data
    else:
        return default

foo = getListBetter("bad data")
foo.append(0)
bar = getListBetter("also bad")
bar.append(1)
print("Foo:", foo)
print("Bar:", bar)
    


assert foo is bar
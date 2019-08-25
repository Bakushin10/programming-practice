import logging
from pprint import pprint
from sys import stdout as STDOUT
"""
https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
"""
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value

class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)

    def times_two(self):
        return self.value * 2

foo = MyChildClass()
print(foo.times_two())

class TimesTwo(object):
    def __init__(self):
        self.value *= 2

class PlusFive(object):
    def __init__(self):
        self.value += 5

class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo = OneWay(5)
print('First ordering is (5 * 2) + 5 =', foo.value)

# Example 5
class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


# Example 6
bar = AnotherWay(5)
print('Second ordering still is', bar.value)

class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5

class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2

class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)
        foo = ThisWay(5)
print("Should be (5 * 5) + 2 = 27 but is", foo.value)

"""
    good way
"""
class MyBaseClass(object):
    def __init__(self, value):
        print("MyBaseClass init'ed")
        self.value = value

class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        print("TimesFiveCorrect init'ed")
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5

    def TimesFiveFunc(self):
        return self.value

class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        print("PlusTwoCorrect init'ed")
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2
    
    def plusTwoFunc(self):
        return self.value

class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        print("GoodWay init'ed")
        super(GoodWay, self).__init__(value)


base = GoodWay(5)
print(base.TimesFiveFunc())
print(base.plusTwoFunc())
# timesFive = TimesFiveCorrect(base)
# plusTwo = PlusTwoCorrect(base)
# g = GoodWay()
print(GoodWay(5))
from pprint import pprint
pprint(GoodWay.mro())
pprint = pprint

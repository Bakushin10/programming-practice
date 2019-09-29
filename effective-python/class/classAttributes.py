# class Field(object):
#     def __init__(self, name):
#         self.name = name
#         self.internal_name = "_" + self.name
    
#     def __get__(self, instance, instance_type):
#         if instance is None: return self
#         return getattr(instance, self.internal_name, "")
    
#     def __set__(self, instance, value):
#         setattr(instance, self.internal_name, value)

# Example 6
class Field(object):
    def __init__(self):
        # These will be assigned by the metaclass.
        self.name = None
        self.internal_name = None
    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)

# Example 4
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                print("{} {} {}".format(key, value, value.name))
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls

# Example 5
class DatabaseRow(object, metaclass=Meta):
    pass

# Example 7
class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()

class BetterCustomer2(object):
    def __init__(self):
        self.__first_name = ""
        # self.__last_name = ""
        # self.__prefix = ""
        # self.__suffix = ""

    def __getattr__(self, name):
        errorTemplate = "{} does not exist"
        setattr(name, "ora!")
        return errorTemplate.format(name)

class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value

# foo = BetterCustomer()
# print('Before:', repr(foo.first_name), foo.__dict__)
# foo.first_name = 'Euler'
# print('After: ', repr(foo.first_name), foo.__dict__)


"""
    python *private* like variable. 
"""
print("*"*10)
foo2 = BetterCustomer2()
print(foo2.__dict__)


# this line raises an error
# print(foo2.__first_name)

# but you can easily get away with it like this....
foo2._BetterCustomer2__first_name = 'Euler'
print(foo2.__dict__)


data = LazyDB()
print('Before:', data.__dict__)
print('foo:   ', data.foo)
print('After: ', data.__dict__)
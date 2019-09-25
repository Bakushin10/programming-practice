class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = "value does not exis so im setting it : {}".format(name)
        setattr(self, name, value)
        return value


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print("Called __getattribute__( % s)" % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            temp = "{} did not exit so variable is being created..."
            print(temp.format(name))
            value = name
            setattr(self, name, value)
        return value

class MissingPropertyDB(object):
    def __getattr__(self, name):
        if name == "bad_name":
            raise AttributeError("{name} is missing")


class BrokenDictionaryDB(object):
    """ 
        The problem is that __getattribute__ accesses self._data, which causes
        __getattribute__ to run again, which accesses self._data again, and so on. The
        solution is to use the super().__getattribute__ method on your instance to fetch
        values from the instance attribute dictionary. This avoids the recursion.
    """
    def __init__(self, data):
        self._data = {}
    
    def __getattribute__(self, name):
        print("called __getattribute__{}".format(name))
        return self._data[name]

from collections import defaultdict
class DictionaryDB(object):
    def __init__(self, data):
        self._data = data
        self.data = ""
    
    def __getattribute__(self, name):
        data_dict = super().__getattribute__("_data")
        errorTemplate = "{} does not exsit"
        return data_dict.get(name, errorTemplate.format(name))


data = LazyDB()
spacetemplate = "{}".format("*"*10)
print("Before:", data.__dict__)
print("foo:", data.foo)
print("foo:", data.foo)
print("After: ", data.__dict__)

print(spacetemplate)
data = ValidatingDB()
print("exists:", data.exists)
print("foo:", data.foo)
print("After: ", data.__dict__)
print("foo:", data.foo)

# print(spacetemplate)
# data = MissingPropertyDB()
# data.bad_name


print("BrokenDictionaryDB" + spacetemplate)
data = BrokenDictionaryDB({"foo": 3})
# data.foo # this breaks

print("DictionaryDB" + spacetemplate)
data = DictionaryDB({"foo": 3})
print(data.foo)
# print("exists:", data.exists)
# print("foo:", data.foo)
# print("After: ", data.__dict__)
# print("foo:", data.foo)
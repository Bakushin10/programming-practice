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

data = LazyDB()
print("Before:", data.__dict__)
print("foo:", data.foo)
print("foo:", data.foo)
print("After: ", data.__dict__)

print(" " * 10)
data = ValidatingDB()
print("exists:", data.exists)
print("foo:", data.foo)
print("After: ", data.__dict__)
print("foo:", data.foo)

print(" " * 10)
data = MissingPropertyDB()
data.bad_name


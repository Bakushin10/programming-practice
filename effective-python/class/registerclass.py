import json

class Serializable(object):
    def __init__(self, *args):
        self.args = args
    
    def serialize(self):
        return json.dumps({"args": self.args})

class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Point2D {} {}".format(self.x, self.y)
    
class Deserializable(Serializable):
    @classmethod
    def deserializable(cls, json_data):
        params = json.loads(json_data)
        return cls(*params["args"])

class BetterSerializable(object):
    def __init__(self, *args, **kwards):
        #print("{} {}".format("args", args))
        self.args =  args
    
    def serialize(self):
        return json.dumps({
            "class" : self.__class__.__name__,
            "args" : self.args
        })
    
    def __rept__(self):
        return "hi"

registry = {}

def register_class(target_class):
    registry[target_class.__name__] = target_class

def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


# Example 7
class EvenBetterPoint2D(BetterSerializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

register_class(EvenBetterPoint2D)

# point = Point2D(5, 3)
# print("Object : ", point)
# print("Serialized : ", point.serialize())
#after = BetterPoint2D.deserialize(data)
point = EvenBetterPoint2D(5, 3)
print('Before:    ', point)
data = point.serialize()
print('Serialized:', data)
after = deserialize(data)
print('After:     ', after)
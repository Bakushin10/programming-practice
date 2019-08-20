names = ["Socrates", "Archimedes", "Plato", "Aristotle"]
names.sort(key=lambda x : len(x))
print(names)

from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0
    
    result = defaultdict(missing,current)
    for key, amount in increments:
        result[key] += amount
    
    return result, added_count

result, count = increment_with_report(current, increments)
print(result)
print(count)


import logging
logging.basicConfig(filename="example.log", level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info("Running "{}" with arguments {}".format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x *y

def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
sub_logger(20,3)
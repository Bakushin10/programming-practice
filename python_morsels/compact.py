from collections import defaultdict

def compact(sequence):
    deduped = []
    for i, item in enumerate(sequence):
        if i == 0 or item != sequence[i-1]:
            deduped.append(item)
    return deduped

"""
"""
def compactWorkWithAnyIterables(iterable):
    """Return new iterable with adjacent duplicate values removed."""
    deduped = []
    previous = None
    for item in iterable:
        if item != previous:
            deduped.append(item)
            previous = item
    return deduped

def a(l):
    for i in l:
        yield i

def compactGenerator(iterable):
    previous = object()
    for item in iterable:
        if item != previous:
            yield item
            previous = item




sequence = [1, 1, 2, 2, 3, 2]
sequence = [1, 1, 1]
print(compactWorkWithAnyIterables(sequence))
l = [n**2 for n in [1, 2, 2]]
print(l)
l = (n**2 for n in [1, 2, 2])

a = a(l)
print(next(a))
print(next(a))
print(next(a))


c = compactGenerator([None, None, 2, 2, 3, 2])

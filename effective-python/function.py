
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
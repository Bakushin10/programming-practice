"""
    for loop expression
"""
# hours_worked = 0
# for event in events:
#     if events.is_billable():
#         hours_worked += event.duration

"""
    generator loop expression
"""
# billable_times = (
#     event.duration
#     for event in events
#     if event.is_billable()
# )

# hours_worked = sum(billable_times)

log_file = [1, 2 , 45, 65, 7, 54, 1, 2 , 45, 65, 7, 54, 1, 2 , 45, 65, 7, 54]
"""
use for 
"""
for i, line in enumerate(log_file):
    if i > 10:
        break
    print(line)

"""
iterator
"""
from itertools import islice
first_ten_line = islice(log_file, 10) # same as log_file[:10]
for line in first_ten_line:
    print(line)



def square_all(numbers):
    for n in numbers:
        yield n**2
favorite_numbers = [6, 57, 4, 7, 68, 95]
square = square_all(favorite_numbers)
print("")
print(next(square))

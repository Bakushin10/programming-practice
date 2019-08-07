import sys

def my_range(n):
    print("my_stasrt starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1

big_range = range(5)
print(big_range)

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

big_list = []

for val in big_range:
    big_list.append(val)
print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)


print("looping again...or not")
for i in my_range(5):
    print("i is {}".format(i))
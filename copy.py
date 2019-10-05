a = [[2, 1, 4], [5, -9, 2], [3, 0, 8], [-2, 6, -4], [-2, 0, -4]]
b = [1,2,3,4]

sorted(b)
sorted(a, key = lambda x: x[0])
copy.deepcopy(list(filter(lambda x: x[0]>4, a)))

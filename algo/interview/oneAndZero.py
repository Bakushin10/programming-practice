def func(arr):
    ones = 0
    zeros = 0
    for i in arr:
        if i == 0:
            zeros += 1
        else:
            ones += 1

    myZeros = 0
    myOnes = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            myOnes += 1
            ones -= 1
        else:
            myZeros += 1
            zeros -= 1
        if myOnes - myZeros > ones - zeros:
            return i+1

arr = [1,1,1,0,1]
arr = [0,0,1,1,0]
print(func(arr))


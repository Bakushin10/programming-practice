"""
https://www.algoexpert.io/questions/Search%20For%20Range
"""
def searchForRange(array, target):
    # Write your code here.
    right = searchForRangeHelper(array, target, 0, len(array), True)
    print(right)

def searchForRangeHelper(array, target, right, left, goLeft):
    if right > left:
        return

    middle = (right + left)/2
    
    if array[middle] < target:
        searchForRangeHelper(array, target, middle+1, left, goLeft)
    elif array[middle] > target:
        searchForRangeHelper(array, target, right, middle-1, goLeft)
    else:
        if goLeft:
            if middle == 0 or array[middle-1] != target:
                print(array[middle-1])
                return middle
            else:
                searchForRangeHelper(array, target, right, middle-1, goLeft)
        else:
            if middle == len(array) - 1 or array[middle + 1] != target:
                print(array[middle-1])
                return middle
            else:
                searchForRangeHelper(array, target, middle+1, middle, goLeft)

    



arr = [0,1,21,33,45,45,45,45,45,61,71,73]
target = 45
searchForRange(arr, target)
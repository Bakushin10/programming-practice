def searchForRange(array, target):
    # Write your code here.
    right = findRight(array, target)
    left = findLeft(array, target)
    
    print(str(right) + " " + str(left))
    return[right, left]

def findLeft(array, target):
    right = 0
    left = len(array)
    while right <= left:
        mid = (right + left)/2
        print(str(right) + " " + str(left))
        if array[mid] == target and array[mid + 1] != target:
            return mid
        if array[mid] <= target:
            right = mid + 1
        else:
            left = mid - 1
    return -1

def findRight(array, target):
    right = 0
    left = len(array)
    while right <= left:
        mid = (right + left)/2
        if array[mid] == target and array[mid - 1] != target:
            return mid
        if array[mid] < target:
            right = mid + 1
        else:
            left = mid - 1
    return -1

#   [0,1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]
a = [0,1,21,33,45,45,45,45,45,45,61,71,73]
a = [5, 7, 7, 8, 8, 10]
print(searchForRange(a,5))

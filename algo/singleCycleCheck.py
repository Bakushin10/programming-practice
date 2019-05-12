
"""
https://www.algoexpert.io/questions/Single%20Cycle%20Check
"""
def hasSingleCycle(array):
    # Write your code here.
    count = [0 for i in range(len(array))]
    numOfElementVisited = 0
    current = 0
    while numOfElementVisited < len(array):
        print(current)
        count[current] += 1
        if count[current] > 1:
            return False
        
        loopCount = array[current]
        while loopCount != 0:
            if loopCount < 0:
                if current == 0:
                    current = len(array) - 1
                else:
                    current -= 1
                loopCount += 1
            else:
                if current == len(array) - 1:
                    current = 0
                else:
                    current += 1
                loopCount -= 1
        numOfElementVisited += 1
        print(count)
    return current == 0

def hasSingleCycle2(array):
    count = [0 for i in range(len(array))]
    numOfElementVisited = 0
    current = 0
    while numOfElementVisited < len(array):
        count[current] += 1
        if count[current] > 1:
            return False
        current = getNextIndex(current, array)
        numOfElementVisited += 1
    return current == 0

def getNextIndex(current, array):
    jump = array[current]
    nextIndex = (current + jump) % len(array)
    return nextIndex if nextIndex >= 0 else nextIndex + len(array)

arr = [2, 3, 1, -4, -4, 2]
print(hasSingleCycle2(arr))
def kadanesAlgorithm(array):
    # Write your code here.
    maxEndingHere = array[0]
    maxSoFar = array[0]

    for i in range(1, len(array)):
        num = array[i]
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
        print(str(maxEndingHere) + " " + str(maxSoFar))
    return maxSoFar

a = [-2,-3,4,-1,-2,1,5,-3]
#a = [4,-2,-3,-1,-2,1,5,-3]

print(kadanesAlgorithm(a))
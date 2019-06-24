"""
https://www.algoexpert.io/questions/Max%20Sum%20Increasing%20Subsequence
"""
def increasingSubsequence(array):
    maxSum = [array[0]]
    maxIndex = 0
    for i in range(1, len(array)):
        currentMax = array[i]
        for j in range(i):
            if array[j] <= array[i] and currentMax <= maxSum[j] + array[i]:
                currentMax = maxSum[j] + array[i]
        maxSum.append(currentMax)
        if maxSum[-1] > maxSum[maxIndex]:
            maxIndex = len(maxSum) -1
    print(maxSum)
    return maxSum[maxIndex]


array = [10, 70, 20, 30, 50, 11, 30]
print(increasingSubsequence(array))
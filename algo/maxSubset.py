def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not len(array):
        return
    if len(array) == 1:
        return array[0]
        
    maxSum = []
    for i in range(len(array)):
        if i < 2:
            maxSum.append(array[i])
        else:
            n = max(maxSum[-1], array[i] + maxSum[i-2])
            maxSum.append(n)
    print(maxSum)


array = [7,10,12,7,9,14]
maxSubsetSumNoAdjacent(array)

        





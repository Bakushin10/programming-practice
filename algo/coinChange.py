"""
https://www.algoexpert.io/questions/Min%20Number%20Of%20Coins%20For%20Change
"""

def numberOfWaysToMakeChange2(n, denoms):
	ways = [0 for i in range(n+1)]
    ways[0] = 1
    for demon in denoms:
        for i in range(1, len(ways)):
            if i - demon >= 0:
                ways[i] += ways[i - demon]
    return ways[n]


def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    arr = [[0 for i in range(n + 1)] for i in range(len(denoms))]
    denoms = sorted(denoms)
    for i in range(len(denoms)):
        for j in range(1, n+1):
            if i == 0:
                #arr[i][j] = j/denoms[i] if n%denoms[i] == 0 else 0
                arr[i][j] = 1 if j>=denoms[i] else 0
            else:
                print(str(j) + " " + str(denoms[i]))
                
                if j >= denoms[i]:
                    d = denoms[i]
                    arr[i][j] = min(arr[i-1][j], arr[i][j-d]+1)
                else:
                    arr[i][j] = arr[i-1][j]
    for i in arr:
        print(i)
    return arr[-1][-1] if arr[-1][-1] != 0 else -1

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    n,m = 0, 0
    minVal = float("inf")
    ans = []
    while n < len(arrayOne) and m < len(arrayTwo):
        diff = abs(arrayOne[n] - arrayTwo[m])
        if diff < minVal:
            minVal = diff
            ans = [arrayOne[n], arrayTwo[m]]
        if arrayOne[n] == arrayTwo[m]:
            return ans
        elif arrayOne[n] < arrayTwo[m]:
            n += 1
        else:
            m += 1
    print(minVal)
    print(ans)
    return ans
    

n = 3
denoms = [2,1]
a1 = [-1,5,10,20,28,3]
a2 = [26, 134, 135, 15, 17]
#print(numberOfWaysToMakeChange(n, denoms))
smallestDifference(a1, a2)
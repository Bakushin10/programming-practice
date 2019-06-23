"""
https://www.algoexpert.io/questions/Four%20Number%20Sum
"""

def fourNumbersSum(array, target):
    from collections import defaultdict
    allPairSums = defaultdict(list)
    quadruplets = []

    for i, num1 in enumerate(array):
        if i < len(array) - 1:
            j = array[i+1]
            for k in range(i+2, len(array)):
                remain = target - (j + array[k])
                if remain in allPairSums:
                    for s in allPairSums[remain]:
                        quadruplets.append(s + [j, array[k]])
        for p in range(i+1):
            P = j + array[p]
            if P not in allPairSums:
                allPairSums[P] = [[array[p], j]]
            else:
                allPairSums[P].append([[array[p], j]])
    return quadruplets

inp = [7,6,4,-1,1,2]
target = 16
print(fourNumbersSum(inp, target))
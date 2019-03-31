"""
https://www.algoexpert.io/questions/Two%20Number%20Sum
"""

def twoNumberSum(array, targetSum):
    # Write your code here.
    from collections import defaultdict
    dic = defaultdict(int)
    for v in array:
        key = targetSum - v
        if v == dic[v]:return sorted([v, targetSum - v])
        else:dic[key] = key
    return []
    


arr = [4,6]
targetSum = 10

print(twoNumberSum(arr, targetSum))
"""
https://www.algoexpert.io/questions/Two%20Number%20Sum
"""

def twoNumberSum(array, targetSum):
    # Write your code here.
    from collections import defaultdict
    dic = defaultdict(int)
    for v in array:
        key = targetSum - v
        if v == dic[v]:
            return sorted([v, targetSum - v])
        else:
            dic[key] = key
        print(str(v) + " " +str(key) +" " +str(dic))
    return []
    
def twoNumberSum2(array, targetSum):
    # Write your code here.
	seen = []
	for num in array:
		pm = targetSum - num
		if pm in seen:
			return sorted([targetSum - num, num])
		else:
			seen.append(num)
	return []


arr = [4, 6]
targetSum = 10

print(twoNumberSum2(arr, targetSum))
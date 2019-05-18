"""
https://www.algoexpert.io/questions/Powerset
"""
def powerset(array, current, ans):
    ans.append(current)
    for i in range(len(array)):
        newArray = array[i+1:]
        cur = current + [array[i]]
        powerset(newArray,cur,ans)
    return ans

def permutation(array, current, ans):
    ans.append(current)
    for i in range(len(array)):
        newArray = array[:i] + array[i+1:]
        cur = current + [array[i]]
        powerset(newArray, cur, ans)
    return ans


arr = [1,2]
print(powerset(arr, [], []))
print(permutation(arr, [], []))
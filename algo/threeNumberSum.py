"""
https://www.algoexpert.io/questions/Three%20Number%20Sum
"""
def threeNumberSum(array, targetSum):
    # Write your code here.
     ans = []
     for num1 in range(len(array)):
          for num2 in range(len(array)):
               if num1 != num2:
                    num3 = targetSum - array[num1] - array[num2]
                    if num3 in array and (array[num2] != num3 and array[num1] != num3):
                         ans.append(sorted([array[num1], array[num2], num3]))
     r = []
     for sublist in ans:
          if sublist not in r:
               r.append(sublist)
     print(r)


array = [12,3,1,2,-6,5,-8,6]
target = 0
threeNumberSum(array, target)
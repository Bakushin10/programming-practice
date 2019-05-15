"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
"""
def canThreePartsEqualsSum(A):
    target = sum(A)/3
    right, left = len(A)-1, 0
    leftSum, rightSum = 0, 0

    while left < right:
        leftSum += A[left]
        if leftSum == target:
            break
        left += 1
    
    while left < right:
        rightSum += A[right]
        if rightSum == target:
            break
        right -= 1
    
    print("---")
    print(left)
    print(right)
    print("L :" + str(leftSum))
    print("R :" + str(rightSum))
    print("M :" + str(sum(A[left+1:right])))
    return leftSum == sum(A[left+1:right]) == rightSum


inp = [0,2,1,-6,6,-7,9,1,2,0,1]

print(canThreePartsEqualsSum(inp))

"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
"""
def canThreePartsEqualsSum(A):
    target = sum(A)/3
    right, left = len(A)-1, 0

    while left < right:
        if sum(A[:left]) == target:
            break
        left += 1
    
    while left < right:
        if sum(A[right:]) == target:
            break
        right -= 1
    
    print("---")
    print(left)
    print(right)
    print("L :" + str(sum(A[:left])))
    print("R :" + str(sum(A[right:])))
    print("M :" + str(sum(A[left:right])))
    return A[:left] == A[left:right] == A[right:]


inp = [0,2,1,-6,6,-7,9,1,2,0,1]

canThreePartsEqualsSum(inp)

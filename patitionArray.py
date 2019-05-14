"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
"""
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        left = 0
        right = len(A)
        while left < right:
            print(str(A[:left]) + " :" + str(sum(A[:left])))
            print(str(A[left:right]) + " :" + str(sum(A[left:right])))
            print(str(A[right:]) + " :" + str(sum(A[right:])))
            print("")
            if sum(A[:left]) == sum(A[left:right]) == sum(A[right:]):
                return True
            if sum(A[:left]) == sum(A[right:]):
                left += 1
                right -= 1
            elif sum(A[:left]) > sum(A[right:]):
                right -= 1
            elif sum(A[:left]) < sum(A[right:]):
                left += 1
        return False
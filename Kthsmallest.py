
"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""
class Solution:
    def kthSmallest(self, matrix, k):
        l = []
        for m in matrix:
            l += m
        return sorted(l)[k-1]
        
    
matrix = [
    [ 1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
    ]
k = 8

d = Solution()
d.kthSmallest(matrix, k)
"""
https://leetcode.com/problems/minimum-falling-path-sum/
"""

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        combi = []
        minSum = self.findMinSum(A,0,0,A[0],combi,[])
        return minSum
    
    def findMinSum(self,A, r, c, nextR, combi, current):
        if len(nextR) != 0:
            print(str(nextR)+" "),
        if len(current) == 3:
            combi.append(current)

        for c, val in enumerate(nextR):
            cur = current + [val]
            print(str(val)+" "),
            nextRow = self.ARange(A, r+1, c)
            self.findMinSum(A, r+1, c, nextRow, combi, cur)
        
        return combi
    
    def ARange(self, A, r, c):
        print(str(c))
        if r > len(A)-1:
            nextR = []
        if c == 0:
            nextR = A[r][c:c+2]
        if c == len(A[0])-1:
            nextR = A[r][c-1:c+1]
        nextR = A[r][c-1:c] + A[r][c:c+2]


A = [[1,2,3],[4,5,6],[7,8,9]]

s = Solution()
print(s.minFallingPathSum(A))
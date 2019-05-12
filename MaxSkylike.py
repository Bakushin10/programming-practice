"""
https://leetcode.com/problems/max-increase-to-keep-city-skyline/
"""
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        LEN = len(grid[0])
        vertical = [0 for i in range(len(grid))]
        horizontal = [0 for i in range(LEN)]

        # get the vertical skyline
        for i in range(LEN):
            hightest = 0
            for j in range(len(grid)):
                if grid[j][i] > hightest:
                    hightest = grid[j][i]
            horizontal[i] = hightest
        
        # get the horizontal skyline
        for i in range(len(grid)):
            hightest = 0
            for j in range(LEN):
                if grid[i][j] > hightest:
                    hightest = grid[i][j]
            vertical[i] = hightest

        total = 0
        for i in range(len(grid)):
            for j in range(LEN):
                preHeight = grid[i][j]
                newHeight = min(vertical[i], horizontal[j])
                total += (newHeight - preHeight)
        return total


grid = [ 
    [3, 0, 8, 4], 
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0]
]
s = Solution()
s.maxIncreaseKeepingSkyline(grid)
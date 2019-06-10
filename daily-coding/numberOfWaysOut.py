"""
There is an N by M matrix of zeroes.
Given N and M, write a function to count the number of ways of starting
at the top-left corner and getting to the bottom-right corner.
You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2,
since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

"""

def findNumOfWaysOut(n, m):
    n = n+1
    m = m+1
    grid = [[0 for j in range(n)] for i in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 1 or j == 1:
                grid[i][j] = 1
            if i == 2 or j == 2:
                grid[i][j] = max(i, j)
            if i > 2 and j > 2:
                grid[i][j] = grid[i][j - 1] + grid[i-1][j]
    
    # for i in range(m):
    #     print(grid[i])

    return grid[-1][-1]

n = 5
m = 5
print(findNumOfWaysOut(m, n))
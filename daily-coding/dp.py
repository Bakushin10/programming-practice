"""
You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down,
find the maximum number of coins you can collect by the bottom right corner.

0 3 1 1
2 0 0 4
1 5 3 1

ans : 12
"""

def dp(array):
    col = len(array)
    row = len(array[0])
    grid = [[0]*row for i in range(col)]
    for i in range(col):
        for j in range(row):
            if i == 0 or j == 0:
                grid[i][j] = array[i][j]
            else:
                grid[i][j] = array[i][j] + max(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


array = [[0,3,1,1],[2,0,0,4],[1,5,3,1]]
print(dp(array))
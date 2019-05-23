"""
https://leetcode.com/problems/max-area-of-island/
"""
def maxAreaOfIsland(grid):
    row = len(grid[0])
    col = len(grid)
    visited = [[False for j in range(row)] for i in range(col)]
    
    maxIsland = 0
    for i in range(col):
        for j in range(row):
            maxIsland = max(maxIsland, findMaxIsland(i, j, grid, visited))
    return maxIsland

def findMaxIsland(col, row, grid, visited):
    if visited[col][row]:
        return 0
    if grid[col][row] == 0:
        visited[col][row] = True
        return 0
    print("get here")
    Q = [(col, row)]
    island = 0
    while Q:
        top = Q.pop(0)
        neighbors = checkNeighbors(top[0], top[1], grid, visited)
        print("nei"+ str(neighbors))
        for neighbor in neighbors:
            Q.append(neighbor)
        visited[top[0]][top[1]] = True
        island += 1
    return island

def checkNeighbors(col, row, grid, visited):
    #left, up, right, down
    X = [-1, 0, 1, 0]
    Y = [0, -1, 0, 1]
    validNeighbors = []
    for i in range(4):
        newX = row + X[i]
        newY = col + Y[i]
        if newX >= 0 and newX < len(grid[0]) and newY >= 0 and newY < len(grid):
            if not visited[newY][newX] and grid[newY][newX] == 1:
                validNeighbors.append((newY, newX))
                visited[newY][newX] = True
    return validNeighbors


grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
# grid = [
#     [1,1,0,0,0],
#     [1,1,0,0,0],
#     [0,0,0,1,1],
#     [0,0,0,1,1]]


print(maxAreaOfIsland(grid))
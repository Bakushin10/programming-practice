def printGrid(grid):

    visited = [[False for i in range(grid[0])] for i in range(len(grid))]
    direction = 4
    row = len(grid)
    col = len(grid[0])
    current = (0,0)
    while hasNext(grid):
        if direction%4 == 0:
            current = goRight(grid, visited, col, current[0])
        if direction%4 == 1:
            current = goDown(grid, visited, col[1], row])


def goDown(grid, visited, col, row):
    for i in row:
        if not visited[i][col]:
            print(grid[i][col])
            visited[i][col] = True
        else:
            return [i, col]
    return [i, col]


def goRight(grid, visited, col, row):
    for i in col:
        if not visited[row][i]:
            print(grid[row][i])
            visited[row][i] = True
        else:
            return [row, i]
    return [row, i]

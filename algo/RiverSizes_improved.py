def riverSizes(matrix):
    sizes = []
    visited = [[False for values in row] for row in matrix]
    visited = [[False for values in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i,j,matrix, visited, sizes)
    return sizes

def traverseNode(y, x, matrix, visited, sizes):
    currentRiverSize = 0
    #stack
    nodesToExplore = [[y,x]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        y = currentNode[0]
        x = currentNode[1]

        # if the node is already visited, then skip
        # if it has not been visited, then mark as visited
        if visited[y][x]:
            continue 
        visited[y][x] = True

        # if the node is 0, then skip it
        if matrix[y][x] == 0:
            continue
        currentRiverSize += 1
        unVisistedNeighbors = getUnvisitedNeighbors(y, x, matrix, visited)
        for neighbor in unVisistedNeighbors:
            nodesToExplore.append(neighbor)
        
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getUnvisitedNeighbors(y, x, matrix, visited):
    unVisistedNeighbors = []

    #top
    if y > 0 and not visited[y-1][x]:
        unVisistedNeighbors.append([y-1, x])
    if y < len(matrix) - 1 and not visited[y+1][x]:
        unVisistedNeighbors.append([y+1, x])
    if x > 0 and not visited[y][x-1]:
        unVisistedNeighbors.append([y, x-1])
    if x < len(matrix[0]) - 1 and not visited[y][x+1]:
        unVisistedNeighbors.append([y,x+1])
    return unVisistedNeighbors

matrix = [
    [1,0,0,1,0],
    [1,0,1,0,0],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,1,1,1,0],
]

print(riverSizes(matrix))
"""
https://www.algoexpert.io/questions/River%20Sizes 

naive way of sovling question. Big O is too slow
"""
from collections import defaultdict
def riverSizes(matrix):
    # Write your code here.
    print(len(matrix))
    print(len(matrix[2]))
    visited = defaultdict(list)
    rivers = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
           if matrix[r][c] == 1 and hasVisited(visited,r, c):
               river = riverSizeHelper(r,c, visited, matrix, 0)
               print("river " +str(river) + "at " + str(r) + "," + str(c))
               print(visited)
               rivers.append(river)
    print(rivers)
    return rivers

def riverSizeHelper(r,c, visited, matrix, riverLen):
    X = [0,0,1,0,-1]
    Y = [0,1,0,-1,0]
    print(str(r) +","+ str(c))
    for i in range(5):
        X_NEXT = c + X[i]
        Y_NEXT = r + Y[i]
        if (X_NEXT >= 0 and X_NEXT < len(matrix[c])) and (Y_NEXT >= 0 and Y_NEXT < len(matrix)) and hasVisited(visited,Y_NEXT, X_NEXT):
            if (matrix[Y_NEXT][X_NEXT] == 1):
                visited[Y_NEXT].append(X_NEXT)
                riverLen = riverSizeHelper(Y_NEXT, X_NEXT, visited, matrix, riverLen + 1)
    return riverLen
    
def hasVisited(visited,y,x):
    yl = visited[y]
    if x not in yl:
        return True
    else:
        return False

matrix = [
    [1,0,0,1,0],
    [1,0,1,0,0],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,1,0],
]

matrix = [
    [1,0,1,1,0,1,1]
]

matrix = [
    [1,0,0,1,0,1,0,0,1,1,1,0],
    [1,0,1,0,0,1,1,1,1,0,1,0],
    [0,0,1,0,1,1,0,1,0,1,1,1],
    [1,0,1,0,1,1,0,0,0,1,0,0],
    [1,0,1,1,0,0,0,1,1,1,0,1]
]

riverSizes(matrix)
def findRedundantConnection(edges):
    parent = [0] * len(edges)

    def find(x):
        if parent[x] == 0:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        print(str(rootX) + " " + str(rootY))
        if rootX == rootY:
            return False
        parent[rootX] = rootY
        return True
        
    for x, y in edges:
        print(str(x - 1) + " " + str(y - 1))
        if not union(x - 1, y - 1): 
            return [x, y]
        print(parent)
        print("")

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
#edges = [[1,2], [1,3], [2,3]]
print(findRedundantConnection(edges))
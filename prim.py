def createAdjMatrix(V, G):
  adjMatrix = []
  
  # create N x N matrix filled with 0 edge weights between all vertices
  for i in range(0, V):
    adjMatrix.append([])
    for j in range(0, V):
      adjMatrix[i].append(0)
      
  # populate adjacency matrix with correct edge weights
  for i in range(0, len(G)):
    adjMatrix[G[i][0]][G[i][1]] = G[i][2]
    adjMatrix[G[i][1]][G[i][0]] = G[i][2]
    
  return adjMatrix

def prims(V, G):
  
  # create adj matrix from graph
  adjMatrix = createAdjMatrix(V, G)
  print(adjMatrix)
  vertex = 0 #initial vertex
  visited = []
  
  while len(visited) != V:
      visited.append(vertex)
      shortest = float("inf")
      vertex = 0

      for v in visited:
          edge = adjMatrix[v]
          for i, e in enumerate(edge):
              if e != 0 and e < shortest and i not in visited:
                  shortest = e
                  vertex = i
      print(visited)
      print(shortest)

  
# graph vertices are actually represented as numbers
# like so: 0, 1, 2, ... V-1
a, b, c, d, e, f = 0, 1, 2, 3, 4, 5

# graph edges with weights
# diagram of graph is shown above
graph = [
  [a,b,2],
  [a,c,3],
  [b,d,1],
  [b,c,5],
  [b,e,4],
  [c,e,4],
  [d,e,2],
  [d,f,3],
  [e,f,5]
]

# pass the # of vertices and the graph to run prims algorithm
print(prims(6, graph)) 
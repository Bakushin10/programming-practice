
def BombEnemy(grid):
    R, C = len(grid[0]), len(grid)
    res, rowKills = 0, 0
    colKills = [0]*R
    
    for i in range(C):
        for j in range(R):
            if j == 0 or grid[i][j-1] == "W":
                rowKills = 0
                for k in range(j, R):
                    if grid[i][k] == "W":
                        break
                    if grid[i][k] == "E":
                        rowKills += 1
            
            if i == 0 or grid[i-1][j] == "W":
                colKills[j] = 0
                for k in range(i, C):
                    if grid[k][j] == "W":
                        break
                    if grid[k][j] == "E":
                        colKills[j] += 1

            if grid[i][j] == "0":
                print("rowKills = {} colKills = {} [{}][{}]".format(rowKills, colKills[j], i, j))
                res = max(res, rowKills + colKills[j])
    print(res)

inp = [["E","E","E","0"],
       ["E","0","0","W"],
       ["0","0","0","0"],
       ["0","0","0","E"]]
BombEnemy(inp)

"""

def BombEnemy(grid):
    R, C = len(grid[0]), len(grid)
    res, rowKills = 0, 0
    colKills = [0]*R
    
    for i in range(C):
        for j in range(R):
            if j == 0 or grid[i][j-1] == "W":
                rowKills = 0
                for k in range(j, R):
                    if grid[i][k] == "W":
                        break
                    if grid[i][k] == "E":
                        rowKills += 1
            #print("rowKills = {}".format(rowKills))
            
            if i == 0 or grid[i-1][j] == "W":
                colKills[j] = 0
                for k in range(j, C):
                    if grid[k][j] == "W":
                        break
                    if grid[k][j]:
                        colKills[j] += 1

            if grid[i][j] == "0":
                print("rowKills = {} colKills = {} [{}][{}]".format(rowKills, colKills[j], i, j))
                res = max(res, rowKills + colKills[j])
    print(res)



"""

def longestCommonStrig(str1, str2):
    grid = [[0]*len(str1) for i in range(len(str2))]
    
    for i in range(len(grid[0])):
        if str2[0] == str1[i]:
            grid[0][i] = 1

    for i in range(len(str2)):
        if str2[i] == str1[0]:
            grid[i][0] = 1

    for i in range(1, len(str2)):
        for j in range(1, len(str1)):
            if str2[i] == str1[j]:
                grid[i][j] = grid[i-1][j-1]+1
            

    for i in grid:
        print(i)
        


str1 = "ABABC"
str2 = "BABCA"

longestCommonStrig(str1, str2)
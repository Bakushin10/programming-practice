def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    arr = [[0 for i in range(n + 1)] for i in range(len(denoms))]
    denoms = sorted(denoms)
    for i in range(len(denoms)):
        for j in range(1, n+1):
            if i == 0:
                #arr[i][j] = j/denoms[i] if n%denoms[i] == 0 else 0
                arr[i][j] = 1 if j>=denoms[i] else 0
            else:
                print(str(j) + " " + str(denoms[i]))
                
                if j >= denoms[i]:
                    d = denoms[i]
                    arr[i][j] = min(arr[i-1][j], arr[i][j-d]+1)
                else:
                    arr[i][j] = arr[i-1][j]
    for i in arr:
        print(i)
    return arr[-1][-1] if arr[-1][-1] != 0 else -1


n = 3
denoms = [2,1]
print(numberOfWaysToMakeChange(n, denoms))
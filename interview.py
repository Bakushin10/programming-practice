def duplicate(arr):
    """
        [1, 2, 3, 1, 4, 5, 2]
        1, 2
    """

    duplicate = []
    for i in range(len(arr)):
        target = arr[i]
        ocur = arr.count(target)
        if ocur > 1 and target not in duplicate:
            print(target)
            duplicate.append(target)

def findSumCombination(arr, target):
    """
        [5, 2, 3, 1, 4, 6, 0]
        target : 5
        5 + 0
        2 + 3
        1 + 4
    """
    for i in range(len(arr)):
        if arr[i] < target:
            for j in range(len(arr)):
                if arr[i] + arr[j] == target:
                    print(str(arr[i]) + " " + str(arr[j]))



if __name__ == "__main__":
    arr = [5, 2, 3, 1, 4, 6, 0]
    #duplicate(arr)
    findSumCombination(arr, 5)
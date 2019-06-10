"""
Given a 2D matrix of characters and a target word, write a function that
returns whether the word can be found in the matrix by going left-to-right,
or up-to-down.

For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

 and the target word 'FOAM', you should return true,
 since it's the leftmost column. Similarly, given the target word 'MASS',
 you should return true, since it's the last row.
"""

def findAWordInArray(array, target):
    row = len(array[0])
    col = len(array)
    for i in range(row):
        for j in range(col):
            # checking the left-to-right
            if array[i][j] == target[0] and row - j >= len(target):
                if target == "".join(array[i][j:j+len(target)]):
                    return True
            # checking the top-to-down
            if array[i][j] == target[0] and col - i >= len(target):
                if isVerticalWord(array, i, j, target):
                    return True
    return False

def isVerticalWord(array, i, j, target):
    verticalStr = ""
    for a in range(len(target)):
        verticalStr += array[i+a][j]
    print(verticalStr)
    print(target)
    return True if verticalStr == target else False


array = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
    ]

target = "ABNA"

print(findAWordInArray(array, target))
"""
https://www.algoexpert.io/questions/Knapsack%20Problem
"""

def knapsackProblem(items, capacity):
    # Write your code here.
    values = [[0 for j in range(capacity+1)] for i in range(len(items)+1)]
    
    for i in range(len(items)+1):
        print(values[i])

    for i in range(1, len(items)+1):
        value = items[i-1][0]
        weight = items[i-1][1]    
        for j in range(capacity+1):
            if j >= weight:
                values[i][j] = max(values[i-1][j], values[i-1][j-weight] + value)
            else:
                values[i][j] = values[i-1][j]
    for i in range(len(items)+1):
        print(values[i])
    
def getKnapSackItems(knapSackValues, items):
    sequence = []
    i = len(knapSackValues) - 1
    c = len(knapSackValues[0]) - 1
    while i > 0:
        if knapSackValues[i][c] == knapSackValues[i-1][c]:
            i -= 1
        else:
            sequence.append(i-1)
            c -= items[i-1][1]
            i -= 1
    
    
# "[v,w]"
items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capa = 10
knapsackProblem(items, capa)

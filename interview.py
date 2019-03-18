"""
    random problems for the interview
"""
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

def minDepth(root):
    
    if root == None:
        return 1
    if root.right is None and root.left is None:
        return 1

    if root.right:
        minDepth(root.right) + 1
    if root.left:
        minDepth(root.left) + 1
    return root + 1

def rangeFunc():
    """
        range(start, stop, step)
    """
    for i in range(1, 10, 1):
        print(i)

def magicNumber(n):

    res = 1
    for i in range(n/2+1):
        res = res*5
        print(res)
    
    if n%2 == 1 and n !=1:
        return res + 5
    else:
        return res

def dijsktra(graph, INF):

    """
        at the beginning, only append the first node with distance of 0.
        If the node does not exist, then append it with the distance of INF.
        For this code, I provided all the nodes with distance for simplicities
    """
    visited =[]
    q = Queue()
    q.put("A")
    dict = {"A":0,"B":INF,"C":INF,"D":INF,"E":INF,"F":INF,"G":INF}
    while not q.empty():
        currntNode = q.get()
        visited.append(currntNode)
        for node, distanceToNextNode in graph[currntNode].items():
            if node not in visited:
                q.put(node) # append Queue
                distanceToCurrentNode = dict.get(currntNode)
                maxDis = dict.get(node) # Max distance to currentNode
                newDistance = distanceToCurrentNode + distanceToNextNode
                if newDistance < maxDis:
                    dict[node] = newDistance
        print(dict)

import math
from Queue import Queue
if __name__ == "__main__":
    arr = [5, 2, 3, 1, 4, 6, 0]
    distances = {
        'B': {'A': 5, 'D': 1, 'G': 2},
        'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
        'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
        'G': {'B': 2, 'D': 1, 'C': 2},
        'C': {'G': 2, 'E': 1, 'F': 16},
        'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
        'F': {'A': 5, 'E': 2, 'C': 16}
    }
    #duplicate(arr)
    #findSumCombination(arr, 5)
    #print(magicNumber(7))
    INF = float("inf")
    dijsktra(distances, INF)
    rangeFunc()

    nlogn
    logn
    n

    logn
    nlogn
    n

    
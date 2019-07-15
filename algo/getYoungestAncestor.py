"""
https://www.algoexpert.io/questions/Youngest%20Common%20Ancestor
"""

def getYoungestCommonAncestor(topAncestor, desendantOne, desendantTwo):
    depthOne = getDecendantDepth(desendantOne, topAncestor)
    depthTwo = getDecendantDepth(desendantTwo, topAncestor)
    if depthOne > depthTwo:
        return backtrackAncestralTree(desendantOne, desendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(desendantTwo, desendantOne, depthTwo - depthOne)

def getDecendantDepth(desendance, topAncestor):
    """
        function that levels up till desendance finds the targeted ancestor
    """
    depth = 0
    while desendance != topAncestor:
        depth += 1
        desendance = desendance.ancestor
    return depth

def backtrackAncestralTree(lowerDecendant, higherDesendant, diff):
    """
    match the level of two nodes
    """
    while diff > 0:
        lowerDecendant = lowerDecendant.ancestor
        diff -= 1
    """
    find the common ancenstor
    """
    while lowerDecendant != higherDesendant:
         lowerDecendant = lowerDecendant.ancestor
         higherDesendant = higherDesendant.ancestor
    return lowerDecendant



def getYoungestCommonAncestor2(topAncestor, desendantOne, desendantTwo):
    depthOfDesendantOne = getDepth(desendantOne)
    depthOfDesendantTwo = getDepth(desendantTwo)
    
    if depthOfDesendantOne > depthOfDesendantTwo:
        levelUp(desendantOne, depthOfDesendantOne - depthOfDesendantTwo)
    else:
        levelUp(desendantTwo, depthOfDesendantTwo - depthOfDesendantOne)
    
    while desendantOne.ancenstor != desendantTwo.ancenstor:
        desendantOne = desendantOne.ancestor
        desendantTwo = desendantTwo.ancestor
    return desendantOne

def getDepth(desendance):
    count = 0
    while desendance.ancestor != NULL:
        desendance = desendance.ancenstor
        count += 1
    return count

def levelUp(node, level):
    for i in range(level):
        node = node.ancestor
    return node

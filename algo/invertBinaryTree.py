"""
https://www.algoexpert.io/questions/Invert%20Binary%20Tree
"""

# O(n) time | O(n) space
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.right)
        queue.append(current.left)

"""
"""
def invertBianryTreeREcursively(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBianryTreeREcursively(tree.left)
    invertBianryTreeREcursively(tree.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left
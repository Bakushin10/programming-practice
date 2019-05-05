def getPermutations(array):
    # Write your code here.
    permutations = []
    getPermutationsHelper(array, [], permutations)
    print(permutations)
    return permutations


def getPermutationsHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            newPermutation = currentPermutation + [array[i]]
            getPermutationsHelper(newArray, newPermutation, permutations)

a = [1,2,3,4]
getPermutations(a)
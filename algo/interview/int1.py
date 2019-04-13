#reverse the string
def reverse(x):
    output = ""
    for c in x:
        output = c + output

    """  """
    output2 = [None]*len(x)
    output2_index = len(x) - 1
    for c in x:
        output2[output2_index] = c
        output2_index -= 1
    print("".join(output2))


def findMissing(arr1, arr2):
    """
    [4, 12, 9, 5, 6]
    [4, 9, 12, 6]
    """
    numDict = {}
    missing = []
    if len(arr1) <= len(arr2):
        toBeTash = arr1
        toBeChecked = arr2
    else:
        toBeTash = arr2
        toBeChecked = arr1

    for i in toBeTash:
        numDict[i] = True
    for i in toBeChecked:
        if not numDict.get(i):
            missing.append(i)
    return missing

def find_missing2(arr1, arr2):
    missing_items = set(arr1) - set(arr2)
    #assert(len(missing_items) == 1)
    return list(missing_items)
    #print(missing_items[0])

def find_missing3(arr1, arr2):
    xor_sum = 0
    l = arr1 + arr2
    for i in l:
        xor_sum ^= i
    return xor_sum

a1 = [4, 12, 9, 5, 6]
a2 = [4, 9,12,6]

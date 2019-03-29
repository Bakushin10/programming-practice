def largestRange(array):
    # Write your code here.
    
    # sort and remove duplicates
    #
    # runtime O(n)
    #
    #
    array = list(sorted(set(array)))
    start = 0
    curr = 0
    longestDistance = 0
    res = []
    
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return [array[0], array[0]]
    if len(array) == 2:
        return[array[0], array[1]]

    for i in range(len(array)):
        curr = i
        diff = array[i] - array[i-1]
        #check if diff > 1 or last element
        if i > 0 and diff != 1 or i == len(array) - 1:
            distance = curr - start
            if distance >= longestDistance:
                longestDistance = distance

                # case when last element is the longest distance
                if i == len(array) - 1 and diff == 1:
                    res = [array[start], array[curr]]
                else:
                    res = [array[start], array[curr-1]]
                # update the starting point
                start = curr
    print(res)
    return res



st = [8,4,2,10,3,6,7,9,1]
largestRange(st)
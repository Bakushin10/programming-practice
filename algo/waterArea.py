def waterArea(heights):
    # Write your code here.
    """
    build the array of highest wall from the left side
    """
    left = [0]
    right = [0 for i in heights]
    curretMax = 0
    for i, num in enumerate(heights):
        if i > 0:
            curretMax = max(curretMax, heights[i-1])
            left.append(curretMax)
            
    """
    build the array of highest wall from the right side
    """
    curretMax = 0
    reversedHights = list(reversed(heights))
    for i, num in enumerate(reversedHights):
        if i > 0:
            print(heights[i-1])
            curretMax = max(curretMax, reversedHights[i-1])
            right[len(heights)-1-i] = curretMax

    """
    build the array of highest wall from the left side
    """
    ans = []
    for i, num in enumerate(heights):
        m = min(left[i], right[i])
        if m > num:
            ans.append(m-num)
        else:
            ans.append(0)
    print(left)
    print(right)
    print(ans)

heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
waterArea(heights)
def largestProcut(stones):

    # largest = 0
    # while nums:
    #     num1 = nums.pop(0)
    #     for i in range(1, len(nums)):
    #         largest = max(largest, num1*nums[i]*nums[i-1])
    # return largest


    print(stones)
    while len(stones) > 1:
        stones = sorted(stones)
        print(stones)
        x = stones.pop(-1)
        y = stones.pop(-1)
        if x != y:
            stones.append(abs(x-y))
    return stones if len(stones) != 0 else 0

nums = [2,2]
print("final " + str(largestProcut(nums)))
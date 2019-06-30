"""
https://leetcode.com/problems/maximum-product-subarray/
"""
def maxProductArray(nums):
    max_prod, min_prod, max_prev, min_prev, cur_max = nums[0], nums[0],nums[0], nums[0],nums[0]
    for i in range(1, len(nums)):
        max_prod = max(max_prev*nums[i], min_prev*nums[i], nums[i])
        min_prod = min(max_prev*nums[i], min_prev*nums[i], nums[i])
        max_prev = max_prod
        min_prev = min_prod
        print("max_prod : " + str(max_prod))
        print("min_prod : " + str(min_prod))
        cur_max = max(max_prod, cur_max)
    print(cur_max)

array = [2, 3, -2, 4, -1]
maxProductArray(array)
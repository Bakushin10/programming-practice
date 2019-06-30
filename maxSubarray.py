"""
https://leetcode.com/problems/maximum-average-subarray-i/
"""
def maxSubarray(nums):
    curMax = nums[0]
    maxSum = nums[0]
    for i in range(1, len(nums)):
        curMax = max(curMax+nums[i], nums[i])
        maxSum = max(maxSum, curMax)
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubarray(nums)

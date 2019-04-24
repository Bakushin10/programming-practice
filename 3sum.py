"""
https://leetcode.com/problems/3sum/
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = []
        self.threeSumhelper(nums, sol)
    
    def threeSumhelper(self, nums, sol = []):

        s = sum(sol)
        print(nums)
        if len(sol) == 3 and s == 0:
            print(sol)
        elif len(sol) >= 3:
            return

        for i in range(len(nums)):
            n = nums[i]
            remaining = nums[i+1:]
            return self.threeSumhelper(remaining, sol + [n])

    def subset_sum(self, numbers, partial=[]):
        s = sum(partial)
        print(partial)
        # check if the partial sum is equals to target
        if len(partial) == 3 and s == 0:
            print(partial)
        if s >= 3:
            return  # if we reach the number why bother to continue

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i+1:]
            self.subset_sum(remaining, partial + [n])

nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
#s.subset_sum(nums,[])
s.threeSumhelper(nums,[])

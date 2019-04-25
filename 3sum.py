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
        ans = []
        return self.threeSumhelper(nums, sol, ans)
       
    def threeSumhelper(self, numbers, partial = [], ans = []):
        if len(partial) == 3 and sum(partial) == 0:
            return ans.append(partial)
        elif len(partial) >= 3:
            return

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i+1:]
            ans = self.threeSumhelper(remaining, partial + [n])
        return ans
    


nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
#s.subset_sum(nums,[])
s.threeSumhelper(nums,[])

"""
https://leetcode.com/problems/3sum/
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = self.threeSumhelper(nums, [], [])
        return list(set(tuple(i) for i in ans))
        
    def threeSumhelper(self, numbers, partial = [], ans = []):
        if len(partial) == 3 and sum(partial) == 0:
            return ans.append(sorted(partial))
        elif len(partial) >= 3:
            return

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i+1:]
            ans = self.threeSumhelper(remaining, partial + [n])
        return ans



nums = [0]
s = Solution()
#s.subset_sum(nums,[])
print(s.threeSum(nums))

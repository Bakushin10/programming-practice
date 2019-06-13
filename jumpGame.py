"""
https://leetcode.com/problems/jump-game/
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return self.canJumpHelper(0, nums)
    
    def canJumpHelper(self, current, nums):
        print(nums[current:])
        if current == len(nums)-1:
            return True
        if current >= len(nums):
            return

        for i in range(nums[current]):
           # print("i = " + str(i))
            if self.canJumpHelper(current + i + 1, nums):
                return True
        return False


lst = [2,3,1,1,4]
lst = [3,2,1,0,4]
lst = [4,9,0,7,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
s = Solution()
print(s.canJump(lst))
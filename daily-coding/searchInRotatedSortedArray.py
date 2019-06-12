"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min = self.findMin(nums)
        a = self.binarySearch(nums[:min], target)
        b = self.binarySearch(nums[min:], target)
        
        if a == -1 and b == -1:
            return -1
            
        if a != -1:
            return a
        else:
            return len(nums[:min]) + b


    def binarySearch(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high)/2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                low = mid+1
            if target < nums[mid]:
                high = mid-1
        
        return -1

    def findMin(self, nums):
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high)/2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return low


nums = [4,5,6,7,0,1,2]
target = 0
s = Solution()
print(s.search(nums, target))
"""
https://leetcode.com/problems/container-with-most-water/
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mostArea = 0
        right = 0
        left = len(height)-1
        while right <= left:
            width = left - right
            hei = min(height[left], height[right])
            currentArea = width * hei
            mostArea = max(mostArea, currentArea)
            if height[right] > height[left]:
                left -= 1
            else:
                right += 1
        return mostArea
area = [2,3,10,5,7,8,9]
s = Solution()
print(s.maxArea(area))
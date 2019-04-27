"""
https://leetcode.com/problems/intersection-of-two-arrays/
"""
class Solution1(object):
    def intersection(self, nums1, nums2):

        numFound = {}
        ans = set()
        for i in nums1:
            numFound[i] = True
        for i in nums2:
            if numFound.get(i):
                ans.add(i)
        return list(ans)

        


# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# s = Solution()
# print(s.intersection(nums1, nums2))

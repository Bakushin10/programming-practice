class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # m1 = self.getMedian(nums1)
        # m2 = self.getMedian(nums2)
        m = sorted(nums1 + nums2)
        print(m)
        ans = self.getMedian(m)
        return ans[0]

    def getMedian(self, n):
        if len(n) == 0:
            return []
        median = 0
        if len(n) % 2 == 0:
            median = (float(n[len(n)/2]) + float(n[len(n)/2-1]))/2
        else:
            median = float(n[len(n)/2])
        return [median]

s = Solution()
nums1 = [1,3]
nums2 = [2]
print(s.findMedianSortedArrays(nums1,nums2))
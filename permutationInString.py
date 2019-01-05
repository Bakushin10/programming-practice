"""

https://leetcode.com/problems/permutation-in-string/

"""


import collections

class Solution:
    def checkInclusion(self, s1, s2):

        l = len(s1)  # window length
        perm1 = collections.Counter(s1)
        d = collections.Counter(s2[0: l])
        
        if perm1 == d:
            return True

        for i in range(len(s2)):
            perm2 = collections.Counter(s2[i:i+l])
            if perm2 == perm1:
                return True
        return False

s1 = "ab"
s2 = "eidbaooo"

s = Solution()
s.checkInclusion(s1, s2)
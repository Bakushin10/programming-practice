"""
https://leetcode.com/problems/find-common-characters/
"""
from collections import Counter
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        d = Counter(A[0])
        for i in range(1, len(A)):
            print(A[i])
            temp = Counter(A[i])
            newDic = {}
            for i in temp:
                if d.get(i):
                    newDic[i] = min(d[i], temp[i])
            d = newDic
        print(newDic)

A = ["cool","lock","cook"]
s = Solution()
s.commonChars(A)
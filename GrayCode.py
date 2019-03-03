"""
    https://leetcode.com/problems/remove-duplicate-letters/
"""
from collections import defaultdict
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = defaultdict(list) 
        trimmed_string = ""
        #s = list(s).sort()#sorted(s,key=lambda x:(str.lower(x),x))
        trimmed = [eachLetter for eachLetter in s]
        trimmed.sort()
        print(trimmed)
        for i in range(len(trimmed)):
            alf = d.get(trimmed[i])
            if not alf:
                trimmed_string += trimmed[i]
                d[trimmed[i]] = True
        print(trimmed_string)
        return trimmed_string


        

s = Solution()
ss = "cbacdcbc"
s.removeDuplicateLetters(ss)



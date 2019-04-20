"""
https://leetcode.com/problems/isomorphic-strings/
"""

class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        top = {}
        down = {}
        for i in range(len(s)):
            if top.get(s[i]) == None and down.get(t[i]) == None:
                top[s[i]] = t[i]
                down[t[i]] = s[i]
            elif top.get(s[i]) != t[i] and down.get(t[i]) !=s[i]:
                return False
        return True

    # def zip(self):
    #     numbersList = [1, 2, 3]
    #     strList = ['one', 'two', "three"]
    #
    #     result = zip(numbersList, strList)
    #     print(result)
    #     print(result[0])
    #     print(result[0][0])

s = Solution()
s.zip()
s.isIsomorphic("aa", "ab")

"""
    https://leetcode.com/problems/group-anagrams/
"""
class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        dic = defaultdict(list)
        for word in strs:
            dic["".join(sorted(word))].append(word)
        print(list(dic.values()))
                

"""
    https://leetcode.com/problems/wildcard-matching/

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        res = ""
        for i in range(len(p)):
            if p[i] == "*":
                res += getAnyMatch(s,p,i)
            elif p[i] == "?":
                print(p[i])
            else:
                res += p[i]
        print(res)
    
    def getAnyMatch(self, s, p, i):
        

        

        

sol = Solution()
# l = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = "adceb"
p = "*a*b"
sol.isMatch(s, p)
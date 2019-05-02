"""
https://leetcode.com/problems/roman-to-integer/
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        i = 0
        while i < len(s):
            if i == len(s)-1:
                total += roman[s[i]]
            if i+1 < len(s):
                if roman[s[i]] < roman[s[i+1]]:
                    total += (roman[s[i+1]] - roman[s[i]])
                    i +=1
                else:
                    total += roman[s[i]]
            i += 1
        return total

r = "MCMXCIV"
s = Solution()
s.romanToInt(r)
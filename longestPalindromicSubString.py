"""
https://leetcode.com/problems/longest-palindromic-substring/
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = [0,0]
        for i in range(len(s)):
            right = i
            left = i
            while right-1 >= 0 and left+1 < len(s):
                if s[right-1] == s[left+1]:
                    right -= 1
                    left += 1
                    if left - right > longest[1] - longest[0]:
                        longest = [right, left]
                else:
                    right = -1
            
            right = i
            left = i+1
            while right >= 0 and left < len(s):
                if s[right] == s[left]:
                    if left - right > longest[1] - longest[0]:
                        longest = [right, left]
                    right -= 1
                    left += 1
                else:
                    right = -1
        print(longest)
        return s[longest[0]:longest[1]+1]

st = "babad"
s = Solution()
print(s.longestPalindrome(st))
"""
https://leetcode.com/problems/longest-palindromic-substring/
"""
class Solution(object):
    def longestPalindrome(self, s):
        currentLongest = [0,1]
        for i in range(len(s)):
            odd = self.getLongestPalindrome(s,i-1,i+1)
            even = self.getLongestPalindrome(s,i-1,i)
            longest = max(odd, even, key = lambda x: x[1] - x[0])
            currentLongest = max(currentLongest, longest, key = lambda x: x[1] - x[0])
        return s[currentLongest[0]:currentLongest[1]]
    
    def getLongestPalindrome(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return [left+1, right]


st = "z234a5abbba54a32z"
s = Solution()
print(s.longestPalindrome(st))




"""
    def longestPalindrome(self, s):

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

"""
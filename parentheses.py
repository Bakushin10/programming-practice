"""
https://leetcode.com/problems/valid-parentheses/
"""
class Solution1(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []

        for top in s:
            if top in pairs.values():
                stack.append(top)
            elif stack and stack[-1] == pairs[top]:
                    stack.pop()
            else:
                return False
        return stack == []

"""
https://leetcode.com/problems/longest-valid-parentheses/
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        pairs = {"(":")"}
        longest = 0
        current = 0
        i = 0
        while i < len(s):
            print("\n" + str(i) + ":" + str(s[i]))
            if s[i] in pairs.keys() and i+1 < len(s):
                if s[i+1] in pairs.values():
                    i += 1
                else:
                    current = i + 1
            else:
                current = i + 1
            i += 1
            print(str(i) + "-" + str(current))
            longest = max(longest, i - current)
        return longest
        print("longest " + str(longest))

l = ")()())"
l = "()(())"
s = Solution()
s.longestValidParentheses(l)     

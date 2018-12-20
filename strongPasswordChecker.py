import re

class Solution:
    def strongPasswordChecker(self, s):
        """
        https://leetcode.com/problems/strong-password-checker/


        :type s: str
        :rtype: int
        
        1. It has at least 6 characters and at most 20 characters.
        2. It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
        3. It must NOT contain three repeating characters in a row 
           ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
        """

        if self.isLength(s) and self.checkCombination(s) and self.hasThreeRepetitive(s):
            return True
        return False

    def hasThreeRepetitive(self, s):
        count = 1
        prev = None
        hasRepe = False
        for i in s:
            if i == prev:
                count += 1
            else:
                count = 1
            if count == 3:
                hasRepe = True
            prev = i
        return hasRepe

    def isLength(self, s):
        print(len(s))
        if len(s) < 6 and len(s) > 20:
            return False
        else:
            return True
    
    def checkCombination(self, s):
        digit = re.compile('\d')
        lower = re.compile('[a-z]')
        upper = re.compile('[A-Z]')

        if digit.search(s) and lower.search(s) and upper.search(s):
            return True
        return False


st = "ssddsdfffd"
s = Solution()
s.strongPasswordChecker(st)

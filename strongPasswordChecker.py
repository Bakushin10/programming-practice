import re

class Solution:
    def strongPasswordChecker(self, s):
        """
        https://leetcode.com/problems/strong-password-checker/
        :type s: str
        :rtype: int
        """
        wordChanged = 0
        
        wordChanged = self.checkDigit(s) + self.checkLower(s) + self.checkUpper(s)
        wordNeedstoBeSwapped = self.checkThreeRepetitive(s)
        print("wordChanged : " + str(wordChanged))
        print("maxLen : " + str(wordNeedstoBeSwapped))

        if(wordNeedstoBeSwapped == 0):
            if len(s) > 20:
                print(len(s) - 20 + wordChanged)
                return len(s) - 20 + wordChanged
            if len(s) > 5:
                print(wordChanged)
                return wordChanged
            if len(s) == 5 and wordChanged >= 1:
                print(wordChanged)
                return wordChanged 
            if len(s) == 5 and wordChanged == 0:
                print("1")
                return 1
            if len(s) < 5:
                print(6 - len(s))
                return 6 - len(s)
        else: # when there are more than 3 word in a row
            #"1234567890123456Baaaaa"
            #"aaaaaaaaaaaaaaaaaaaaa"
            #"aaa aaa aaa aaa aaa aaa aaa"
            if len(s) > 20:
                if wordNeedstoBeSwapped > wordChanged:
                    print(len(s) - 20 + wordNeedstoBeSwapped)
                    return len(s) - 20 + wordNeedstoBeSwapped
                else:
                    print(len(s) - 20 + wordChanged)
                    return len(s) - 20 + wordChanged
            if len(s) > 5:
                if wordNeedstoBeSwapped > wordChanged:
                    print(wordNeedstoBeSwapped)
                    return wordNeedstoBeSwapped
                else:
                    print(wordChanged)
                    return wordChanged
            if len(s) <= 5:
                print(6 - len(s) + wordNeedstoBeSwapped)
                return 6 - len(s) + wordNeedstoBeSwapped
            
    def checkThreeRepetitive(self, s):
        consec_list = re.findall(r'((\w)\2{2,})', s)
        print(consec_list)
        total = 0
        for i in enumerate(consec_list):
            total += float(len(i[1][0])/3)
        reminder = float(total) - int(total)
        if float(reminder) > 0:
            total += 1
        print(float(reminder))
        print(total)
        return int(total)
    
    def checkDigit(self, s):
        digit = re.compile('\d')
        if digit.search(s):
            return 0
        return 1
    
    def checkLower(self, s):
        lower = re.compile('[a-z]')
        if lower.search(s):
            return 0
        return 1
    
    def checkUpper(self, s):
        upper = re.compile('[A-Z]')
        if upper.search(s):
            return 0
        return 1

st = "1234567890123456Baaaaa" # 22, 1, 0
st = "aaaaaaaaaaaaaaaaaaaaa"  # len = 21, consec = 7, wordneedsto = 2
st = "1111111111"

s = Solution()
s.strongPasswordChecker(st)
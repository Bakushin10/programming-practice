"""
https://leetcode.com/problems/goat-latin/
"""
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = {"a", "i", "u", "e", "o", "A", "I", "U", "E", "O"}
        MA = "ma"
        WORD_A = "a"
        gl = []
        for i, word in enumerate(S.split()):
            if word[0] in vowel:
                temp = word + MA + (WORD_A*(i+1))
            else:
                temp = word[1:] + word[0] + MA + (WORD_A*(i+1))
            gl.append(temp)
        return " ".join(gl)

inp = "The quick brown fox jumped over the lazy dog"
s = Solution()
s.toGoatLatin(inp)
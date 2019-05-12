"""
https://leetcode.com/problems/jewels-and-stones/
"""
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = {}
        total = 0
        for letter in S:
            print(letter)
            if count.get(letter):
                count[letter] += 1
            else:
                count[letter] = 1
        for j in J:
            if count.get(j):
                total += count[j]
        return total

J = "aA"
S = "aAAbbbb"
s = Solution()
s.numJewelsInStones(J,S)
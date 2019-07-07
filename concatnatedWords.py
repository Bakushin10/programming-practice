"""
https://leetcode.com/problems/concatenated-words/
"""
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for word in words:
            count = 0
            i = 0
            while count != 2 and i < len(words):
                if words[i] in word and words[i] != word:
                    count += 1
                if count == 2:
                    ans.append(word)
                i += 1
        return ans


s = Solution()
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
words = ["a","b","ab","abc"]
print(s.findAllConcatenatedWordsInADict(words))
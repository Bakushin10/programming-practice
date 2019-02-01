"""
https://leetcode.com/problems/text-justification/
"""
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        current = []
        res = []
        count = 0
        for i in range(len(words)):
            curWidth = len(words[i])
            space = 0 if len(current) < 1 else len(current) # space between words
            if count + curWidth + space <= maxWidth:
                current.append(words[i])
                count += curWidth
            else:
                print(count + len(current) - 1)
                print(words[i])
                res.append(current)
                current = []
                current.append(words[i])
                count = curWidth
            if i == len(words)-1:
                    res.append(current)

        print(res)




words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
s = Solution()
s.fullJustify(words, maxWidth)

"""
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

"""
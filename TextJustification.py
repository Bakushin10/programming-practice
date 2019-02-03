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
        c = []# keep track of count
        chunk = []
        count = 0
        for i in range(len(words)):
            curWidth = len(words[i])
            space = 0 if len(current) < 1 else len(current) # space between words
            if count + curWidth + space <= maxWidth:
                current.append(words[i])
                count += curWidth
            else:
                chunk.append(current)
                current = []
                current.append(words[i])
                c.append(count)
                count = curWidth
            if i == len(words)-1:
                chunk.append(current)
                c.append(count)

        # add space
        res = []
        for i in range(len(chunk)):
            spaceTofill = len(chunk[i])-1
            space = maxWidth - c[i]
            spaceToAdd = space if spaceTofill == 0 else (space / spaceTofill)
            remain = space if spaceTofill == 0 else (space % spaceTofill)
            s = spaceToAdd + 1
            no_remainder_space = ""
            remainder_space = ""
            l = spaceTofill if spaceTofill > 0 else 1

            # create sting for space to add
            for k in range(s):
                if k+1 < s:
                    no_remainder_space += " "
                remainder_space += " "
            
            for k in range(l):
                loc = 1 if k == 0 else 2*k+1
                if k < remain:
                    chunk[i].insert(loc,remainder_space)
                else:
                    chunk[i].insert(loc,no_remainder_space)
            
            res.append("".join(chunk[i]))
        print(res)
        return res

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
s = Solution()
s.fullJustify(words, maxWidth)

"""
[
   "This    is    an",
   "example  of text",
   "justification.  "
   'This    is    an',
   'example  of text',
   'justification.   '

]

[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

[
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
]

[
    'Science  is  what we',
    'understand      well',
    'enough to explain to',
    'a  computer.  Art is',
    'everything  else  we',
    'do                   '
]


"""
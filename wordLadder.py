"""
https://leetcode.com/problems/word-ladder/
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        count = self.ladderLengthHelper(beginWord, endWord, wordList, 1)
        print(count)

    def ladderLengthHelper(self, currentWord, endWord, wordList, count):
        print(wordList)
        
        if currentWord == endWord:
            return count

        for i, word in enumerate(wordList):
            validword = self.getValidWord(word,currentWord, endWord, False)
            if validword:
                print(validword)
                newWordList = wordList[:i] + wordList[i+1:]
                return self.ladderLengthHelper(validword, endWord, newWordList, count+1)
        return 0

    def getValidWord(self, wordToCheck, currentWord, endWord, checkEndWord): 
        s = endWord if checkEndWord else currentWord
        diff = 0
        for i in range(len(s)):
            if wordToCheck[i] != s[i]:
                diff += 1
            if diff > 1:
                return None
        return wordToCheck



from collections import defaultdict
class Solution1(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        for i in all_combo_dict:
            print(str(i) + " " + str(all_combo_dict[i]))

        # Queue for BFS
        queue = [(beginWord, 1)]
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
        
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
s = Solution1()
s.ladderLength(beginWord, endWord, wordList)

class Trie:
    
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for i in range(len(string) + 1):
            print(string[i:])
            self.populateSuffixTrieFromHelper(string[i:])
            
    def populateSuffixTrieFromHelper(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    def contains(self, string):
        # Write your code here.
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            else:
                node = node[letter]
        if self.endSymbol in node:
            return True
        else:
            return False






    #dictionary like data structure
    head = {}

    def add(self, word):
        node = self.head

        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['*'] = True
        print(self.head)
    
    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True
        else:
            return False

t = Trie("Hello")
# t.add("Hello")
# t.add("Him")

"""
https://www.algoexpert.io/questions/Suffix%20Trie%20Construction
"""

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

	
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
			word = string[i:]
			self.populateSuffixTrieFromHelper(word)

	def populateSuffixTrieFromHelper(self,string):
		node = self.root
		for letter in string:
			#letter = string[j]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = True

		
    def contains(self, string):
		node = self.root
		for letter in string:
			if letter not in node:
				return False
			node = node[letter]
		return self.endSymbol in node


        str1 = "abacbcsss"
        count = {}

        for i in string:
            count[i] += 1
        for i in string:
            if count[i] == 1:
                return i 
        return ""



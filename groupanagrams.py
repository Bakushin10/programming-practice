def groupAnagrams(words):
	# Write your code here.
	from collections import defaultdict
	anagrams = defaultdict(list)
	
	for word in words:
		anagrams["".join(sorted(word))].append(word)
	return list(anagrams.values())

words = ["yo","act","floop","tac","cat","oy","oolfp"]
print(groupAnagrams(words))
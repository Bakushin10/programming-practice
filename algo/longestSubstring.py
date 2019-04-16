def longestSubstringWithoutDuplication(string):
    # Write your code here.
    lastSeen = {}
    longestSubstring = [0,1]
    startInx = 0
    for i, char in  enumerate(string):
        if char in lastSeen:
            startInx = max(startInx, lastSeen[char] + 1)
        if longestSubstring[1] - longestSubstring[0] < i+1 - startInx:
            longestSubstring = [startInx, i+1]

        lastSeen[char] = i
    return string[longestSubstring[0]: longestSubstring[1]]



st = "abc"
print(longestSubstringWithoutDuplication(st))
print(st[::])
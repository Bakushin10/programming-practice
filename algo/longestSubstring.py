def longestSubstringWithoutDuplication(string):
    # Write your code here.
    start = 0
    lastSeen = {}
    longestSubstring = ""
    for i, char in enumerate(string):
        if char in lastSeen:
            ls = lastSeen[char]
            start = max(ls+1, start)
        
        currentSubstring = string[start:i+1]
        if len(currentSubstring) > len(longestSubstring):
            longestSubstring = currentSubstring
        lastSeen[char] = i
        print(longestSubstring)
    print(lastSeen)

def longestPalindromicSubstring(string):
    # Write your code here.
    if len(string) == 0:
        return 
    if len(string) == 1:
        return string
    
    lastSeen = {}
    longestSubString = string[0]
    for i, char in enumerate(string):
        if char in lastSeen:
            lastSeenIndex = lastSeen[char]
            subString = string[lastSeenIndex:i+1]
            if checkPalin(subString) and len(subString) > len(longestSubString):
                longestSubString = subString
        lastSeen[char] = i
    return longestSubString
            
def checkPalin(s):
    ran = len(s) / 2 if len(s) % 2 == 0 else len(s) / 2 + 1
    last = len(s) - 1
    for i in range(ran):
        if s[i] != s[last]:
            return False
        last -= 1
    return True







st = "clementisacap"
st2 = "highnoon"
#longestSubstringWithoutDuplication(st)
print(longestPalindromicSubstring(st2))
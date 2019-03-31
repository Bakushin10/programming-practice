import sys

def wordChain():
    num = sys.stdin.readline()
    words = []
    
    """ if N is not valid """
    try:
        val = int(num)
    except:
        return "not digit or out of range"
    
    """ check the range of N """
    if int(num) <=0 or int(num) > 10:
        return "not digit or out of range"

    """ takes care of edge case """
    if int(num) == 1:
        return 1

    """ get the word input """
    for i in range(int(num)):
        word = sys.stdin.readline()
        words.append(word.replace('\n',''))
    
    count = 0
    consec = 1
    for i, word in enumerate(words):
        if i >=1:
            last = words[i-1][-1]
            start = words[i][0]
            """
                if last char of previous word and 
                the first word of the current word is the same
                then update consec.
                if not, put the concep back to 0
            """
            if last == start:
                consec += 1
                count = max(count, consec)
            else:
                count = max(count, consec)
                consec = 1
    return count
    

print(wordChain())
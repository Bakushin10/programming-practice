def levenshteinDistance(str1, str2):
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2)+1)]
    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i-1][0] + 1
    print(edits)

str1 = "abc"
str2 = "yabd"
levenshteinDistance(str1, str2)
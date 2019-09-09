"""
https://www.techiedelight.com/longest-common-substring-problem/
"""
def longestCommonSubsequence(str1, str2):
	dp = [[0]* len(str2) for i in range(len(str1))]
	ans = []
	for i in range(len(str1)):
		for j in range(len(str2)):
			if i == 0 or j == 0:
				if str1[i] == str2[j]:
					ans.append(str1[i])
					# dp[i][j] = 1
			elif i > 0 and j > 0:
				if str1[i] == str2[j] and j <= i:
					ans.append(str1[i])
	return ans
				


str1 = "XKYKZPW"
str2 = "ZXVVYZW"

print(longestCommonSubsequence(str1, str2))
class Solution(object):
    def moveZeroes(self, s):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(s) == 0: return 0
        from collections import defaultdict
        seen = defaultdict(int)
        seen[s[0]] = 0
        start = 0
        maxLen = 0
        
        for i in range(1, len(s)):
            # we've seen the char previously
            if seen[s[i]] != 0:
                start = max(seen[s[start+1]], seen[s[i]])
            seen[s[i]] = i
            print(str(i) + " " + str(start)+ " :"),
            v = i - start
            print(max(maxLen, v))
            maxLen = max(maxLen, v)
        return maxLen

s = Solution()
nums = "aub"
print(s.moveZeroes(nums))
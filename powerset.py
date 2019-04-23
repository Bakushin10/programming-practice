def bin(nums):
    totalSize = len(nums) * len(nums)

    for n in range(totalSize):
        l = []
        while n:
            l.append(n & 1) # bit by bit and
            n >>= 1 # shift the bit by 1 to the right
        ans = getConbination(l,nums)
        print(ans)

def getConbination(l, nums):
    ans = []
    if len(l) <= len(nums):
        for i, num in enumerate(l):
            if num: ans.append(nums[i])
        return ans


s = [1,2,3]

print(bin(s))
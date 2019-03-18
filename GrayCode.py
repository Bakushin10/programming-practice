"""
    https://leetcode.com/problems/remove-duplicate-letters/
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def back_track(res, nums, i, target, found):
            '''
            :list[list[int]], the result 
            :list[int], the candidate 
            :int, the index of current number that needs to be checked
            :int, the remained target
            :list[int], the list of found numbers 
            '''
            if target < 0:
                return 
            elif target == 0: 
                res.append(found[:])    # because found is a list (mutable), we must add its copy instead of itself
            else:
                # find the next possible number
                for j in range(i,n,1):
                    found.append(nums[j])   # try to add it to 'found' list
                    back_track(res, nums, j, target-nums[j], found)
                    print(str(j) + str(found))
                    found.remove(nums[j])
            return
        
        n = len(candidates)
        # nums = sorted(candidates) # no need in this problem
        nums = candidates
        res = []
        back_track(res, nums, 0, target, [])
        return res

    def findSum(arr, target):
        hi = arr[len(arr) - 1]
        while low < hi:
            low = i
            if  target == arr[hi] + arr[low]:
                return True
            if target < arr[hi]:
                hi -= 1
            if target > arr[low]:


s = Solution()
candidates = [2,3,6,7]
target = 7
s.combinationSum(candidates, target)



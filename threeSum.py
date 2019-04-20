class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        ans = 0
        A.sort()

        """
        same as the 2-pair questions, using 2 pointers right and left.
        takes care of extra cases when there are a duplicate of the same number.

        """
        for i, x in enumerate(A):
            T = target - A[i]
            j,k = i+1, len(A)-1
            while j < k:
                if A[j] + A[k] < T:
                    j += 1
                if A[j] + A[k] > T:
                    k -= 1
                elif A[j] != A[k]:
                    left = right = 1
                    while j + 1 < k and A[j] == A[j+1]:
                        left += 1
                        j += 1
                    while k+1 < k and A[k] == A[k+1]:
                        right += 1
                        k -= 1
                    
                    ans += left * right
                else:
                    ans += (k-j+1) * (k-j) / 2
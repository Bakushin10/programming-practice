from collections import defaultdict

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        d = defaultdict(list)
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
        print(d)
    
inp = [[1,2], [1,3], [2,3]]
s = Solution()
s.findRedundantConnection(inp)
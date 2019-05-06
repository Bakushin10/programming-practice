"""
https://leetcode.com/problems/all-paths-from-source-to-target/
"""

class Solution(object):
    def allPathsSourceTarget(self, graph):
        path = [0]
        return self.allPathsSourceTargetHelper(graph,graph[0], path, [])
        
    def allPathsSourceTargetHelper(self, oriGraph, nodes, path, ans):
        if path[-1] == len(oriGraph)-1:
            ans.append(path)

        for node in nodes:
            newPath = path + [node]
            newNodes = oriGraph[node]
            self.allPathsSourceTargetHelper(oriGraph, newNodes, newPath, ans)
        return ans
        
g =[[1,2], [3], [3], []]
s = Solution()
print(s.allPathsSourceTarget(g))
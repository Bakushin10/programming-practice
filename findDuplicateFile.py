"""
https://leetcode.com/problems/find-duplicate-file-in-system/
"""
from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        dic = defaultdict(list)
        for path in paths:
            path = path.split(" ")
            root = path[0] + "/"
            for i in range(1,len(path)):
                fileName, content = self.getPathToTheFile(path[i])
                completedRoot = root + fileName
                dic[content].append(completedRoot)
        
        # construct the return value
        res = []
        for v in dic:
            r = []
            if len(dic[v]) > 1:
                for i in dic[v]:
                    r.append(i)
                res.append(r)
        return res

    def getPathToTheFile(self, s):
        # get the content, inside of ()
        content = s[s.find("(")+1:s.find(")")]
        # get a file name. ex) 1.txt
        # it is always len(content - 2) because of () 
        fileName = s[:-(len(content)+2)]
        return fileName, content


paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
paths = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
s = Solution()
print(s.findDuplicate(paths))

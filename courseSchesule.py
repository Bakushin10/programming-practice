from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        if len(prerequisites) == 0:
            l = []
            for i in range(numCourses):
                l.append(i)
            return l

        courses = defaultdict(list)
        for [cource,prec] in prerequisites:
            courses[prec].append(cource)

        for start in courses.keys():
            print(start)
            q = [start]
            l = []
            visit = []
            while q:
                prerec = q.pop(0)
                visit.append(prerec)
                if prerec not in l:
                    l.append(prerec)
                courcesToTake = courses[prerec]
                for i in courcesToTake:
                    if i not in visit:
                        q.append(i)
            if len(l) == numCourses:
                return l
        return [0]
    
    

            
#2, [[1,0]]  4 [[1,0],[2,0],[3,1],[3,2]]
c = 4
l = [[1,0],[2,0],[3,1],[3,2]]
s = Solution()
print(s.findOrder(c,l))
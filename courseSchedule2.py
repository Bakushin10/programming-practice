from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):

        courses = defaultdict(list)
        for [cource,prec] in prerequisites:
            courses[prec].append(cource)
        print(courses)
        for start in courses.keys():
            print(start)
            q = [start]
            l = []
            while q:
                prerec = q.pop(0)
                courcesToTake = courses[prerec]
                for i in courcesToTake:
                    print(str(i) + " " + str(courses[i]))
                    if i not in courses[i]:
                        q.append(i)
                        l.append(prerec)

            if len(l) == numCourses:
                return True
        return False

c = 2
l = [[1,0], [0,1]]
s = Solution()
s = Solution()
print(s.canFinish(c,l))
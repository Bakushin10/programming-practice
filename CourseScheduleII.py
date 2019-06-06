"""
https://leetcode.com/problems/course-schedule-ii/
"""
from collections import defaultdict

class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        if len(prerequisites) == 0:
            l = []
            for i in range(numCourses):
                l.append(i)
            return l

        courses = defaultdict(list)
        keys = []
        values = []
        Q = []
        for [course,prerec] in prerequisites:
            courses[prerec].append(course)
            keys.append(course)
            values.append(prerec)

        for i in range(numCourses):
            if (i in values and i not in keys) or (i not in values and i not in keys):
                Q.append(i)

        Q = list(set(Q))
        print(Q)
        print(courses)

        topological_sorted_order = []
        while Q:
            prerec = Q.pop(0)
            if prerec not in topological_sorted_order:
                topological_sorted_order.append(prerec)
            
            for i in courses[prerec]:
                Q.append(i)
        
        return topological_sorted_order if len(topological_sorted_order) == numCourses else []

    def findOrder2(self, numCourses, prerequisites):
        """
            correct solution
            this is not the most optimal solution but one way to solve this question.
        """
        courses = {n: [] for n in range(numCourses)}
        for (courseTotake, prere) in prerequisites:
            courses[courseTotake].append(prere)
        
        # find the starting nodes. 
        Q = [node for node in range(numCourses) if len(courses[node]) == 0]
        
        courseOrder = []
        while Q:
            prerec = Q.pop(0)
            courseOrder.append(prerec)
            #remove the prerec from course
            for i in range(numCourses):
                if prerec in courses[i]:
                    courses[i].remove(prerec)
                    if len(courses[i]) == 0:
                        Q.append(i)
        return courseOrder if len(courseOrder) == numCourses else []

#2, [[1,0]]  4 [[1,0],[2,0],[3,1],[3,2]]
c = 4
l = [[1,0],[2,0],[3,1],[3,2]]

# c = 3
# l = [[0,1],[0,2],[1,2]]

# c = 3
# l = [[1,0]]

s = Solution()
print(s.findOrder2(c,l))

head = LinkedList(0).addMany([1,2,3,4,5,6,7,8,9])
k = 6
print(remvoeKthNode(head,k))
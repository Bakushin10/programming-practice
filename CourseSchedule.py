from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courses = {}
        visited = []

        prereq_dict=defaultdict(list)
        for [k,v] in prerequisites:
            prereq_dict[k].append(v)

        print(prereq_dict)
        for i in range(len(prerequisites)):
            prereq = prerequisites[i][1]
            courseTotake = prerequisites[i][0]
            print(str(courseTotake) + ", " + str(prereq))
            if courseTotake in visited:
                print("false")
                return False
            visited.append(prereq)
            print("visited" +" " + str(visited))
            numCourses = numCourses + 1

            return False
        return True

    # def findCourse(self, courseTotale, prereq, visited):
    #     if courseTotake in visited:
    #         return False
    #     else:
    #         visited.append(prereq)
    #         findCourse()


s = Solution()

input = 3
pre = [[0,2], [1,2], [2,0],[2,1]] # [[0,2], [1,2], [2,0]]
s.canFinish(input, pre)

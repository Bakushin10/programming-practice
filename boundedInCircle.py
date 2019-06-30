"""
https://leetcode.com/problems/robot-bounded-in-circle/discuss/290856/JavaC%2B%2BPython-Let-Chopper-Help-Explain
https://leetcode.com/problems/robot-bounded-in-circle/
"""
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        current = [0,0]
        right, left = 0,0
        right_move = [(0,1),(0,-1)]
        left_move  = [(-1,0),(1,0)]
        current_instruction = "R"
        for instruction in instructions:
            if instruction == "L":
                current_instruction = "L"
                left += 1
            if instruction == "R":
                current_instruction = "R"
                right += 1
            
            if instruction == "G" and current_instruction == "R":
                i = right%2
                current = [current[0] + right_move[i][0], current[1] + right_move[i][1]]
            if instruction == "G" and current_instruction == "L":
                i = left%2
                current = [current[0] + left_move[i][0], current[1] + left_move[i][1]]
            print(current)
                        
s = Solution() 
route = "GGLLGG"
print(s.isRobotBounded(route))
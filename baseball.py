class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        temp = []
        for i in range(len(ops)):
            if ops[i] == "C":
                temp.pop()
            elif ops[i] == "D":
                d = temp[-1]*2
                temp.append(d)
            elif ops[i] == "+":
                temp.append(temp[-1] + temp[-2])
            else:
                temp.append(int(ops[i]))
        return sum(temp)
        
inp = ["5","-2","4","C","D","9","+","+"]
s = Solution()
s.calPoints(inp)
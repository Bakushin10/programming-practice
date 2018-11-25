class Solution:
    signs = ['-', '+', '(']
    mathSigns = ['-', '+']

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = self.getPostfix(s)
       # print(stack)
    
    def getPostfix(self, s):
        output = []
        operator = []
        for i in s:
            if i == ')':
                while operator[-1] != '(':
                    pop = operator.pop()
                    output.append(pop)
                operator.pop()
            elif i not in self.signs: # numbers
                if len(operator) == 0:
                    output.append(i)
                elif operator[-1] in self.mathSigns:
                    pop = operator.pop()
                    output.append(pop)
                    operator.append(i)
                else:
                    output.append(i)
            else:
                operator.append(i)
        
        if operator:
            while len(operator) != 0:
                pop = operator.pop()
                output.append(pop)

        print("operator")
        print(operator)
        print("stack")
        print(output)
        
        return output
        

s = Solution()
equation = "(1+(4+5+2)-3)+(6+8)" # 3.5
s.calculate(equation)
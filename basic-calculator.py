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
            elif i in self.signs: # signs
                if len(operator) == 0:
                    operator.append(i)
                elif operator[-1] in self.mathSigns and i in self.mathSigns:
                    pop = operator.pop()
                    output.append(pop)
                    operator.append(i)
                else:
                    operator.append(i)
            else: # numbers
                output.append(i)
        
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
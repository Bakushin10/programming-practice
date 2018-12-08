class Solution:
    
    #https://leetcode.com/problems/basic-calculator/
    #shunting yard algorithm
    #postfix calculation

    signs = ['-', '+', '(']
    mathSigns = ['-', '+']
    allSigns = ['-', '+', '(',')']
    def calculate(self, s):
        """
        :type s: strfrom treelib import Node, Tree
        :rtype: int
        """
        # take care of the edge cases (1) 0 
        
        s = s.replace(" ","")
        s = self.buildArr(s)
        stack = self.getPostfix(s)
        result = self.postFix(stack)
        print(result)
        return result
    
    def postFix(self, stack):
        s = []
        while len(stack) != 0:
            pop = stack.pop(0)
            if pop in self.mathSigns:
                top = s.pop()
                buttom = s.pop()
                val = self.calc(top, buttom, pop)
                s.append(val)
            else:
                s.append(pop)
        return int(s[0])

    def buildArr(self, s):
        stack = []
        num = ""
        for i in range(len(s)):
            if s[i] in self.allSigns and num == "":
                stack.append(s[i])
            elif s[i] in self.allSigns and num != "":
                stack.append(num)
                stack.append(s[i])
                num = ""
            else:
                num = num + s[i]
        
        if num != "":
            stack.append(num)

        return stack
        
    def calc(self, top, buttom, operator):
        val = 0
        if operator == '+':
            val = int(buttom) + int(top)
        else:
            val = int(buttom) - int(top)
        return val

    def getPostfix(self, s):
        output = []
        operator = []
        for i in range(len(s)):
            if s[i] == ')':
                while operator[-1] != '(':
                    pop = operator.pop()
                    output.append(pop)
                operator.pop()
            elif s[i] in self.signs: # signs
                if len(operator) == 0:
                    operator.append(s[i])
                elif operator[-1] in self.mathSigns and s[i] in self.mathSigns:
                    pop = operator.pop()
                    output.append(pop)
                    operator.append(s[i])
                else:
                    operator.append(s[i])
            else: # numbers
                output.append(s[i])
        
        if operator:
            while len(operator) != 0:
                pop = operator.pop()
                output.append(pop)

        # print("operator")
        # print(operator)
        # print("stack")
        # print(output)
        
        return output
        

s = Solution()
equation = "(1+(4+5+2)-3)+(6+8)" # 3.5
s.calculate(equation)
class Solution:
    signs = ['-', '+', '(']
    mathSigns = ['-', '+']
    allSigns = ['-', '+', '(',')']
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # take care of the edge cases (1) 0 

        s = s.replace(" ","")
        self.buildArr(s)
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

        print(stack)
        
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

        # print("operator")
        # print(operator)
        # print("stack")
        # print(output)
        
        return output
        

s = Solution()
equation = "2147483647+10+(5+4)" # 3.5
s.calculate(equation)
# class Solution:
#     def calculate(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         cur, res, sign, stack = 0, 0, 1, []
#         for c in s:
#             if c.isdigit():
#                 cur = cur*10 + int(c)
            
#             elif c == "+" or c == "-":
#                 res += cur*sign
#                 cur = 0
#                 sign = [-1, 1][c == "+"]
            
#             elif c == "(":
#                 stack.append(res)
#                 stack.append(sign)
#                 sign = 1
#                 res = 0
#                 cur = 0
            
#             elif c == ")":
#                 res += cur*sign
#                 res *= stack.pop()
#                 res += stack.pop()
#                 cur = 0
        
#         return res + sign*cur



#########################################

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        sign = 1
        i = 0

        while i < len(s):
            print(stack)
            print(res)
            if s[i].isspace():
                i += 1
                continue
            elif s[i] == "(":
                stack.append((res, sign))
                res = 0
                sign = 1
            elif s[i] == ")":
                prev_res, prev_sign = stack.pop()
                print(str(prev_res) + " " + str(prev_sign))
                res = res * prev_sign + prev_res
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            else:
                n = 0
                while i < len(s) and s[i].isdigit():
                    n = n * 10 + int(s[i])
                    i += 1
                res += sign * n
                continue
            i += 1
        return res

s = Solution()
equ = "10+(2-(5-1))"
s.calculate(equ)
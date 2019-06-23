class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        count = []
        encoding_string = []
        for element in s:
            if element == "]":
                encoding_str = ""
                while True:
                    pop = stack.pop(-1)
                    if pop != "[":
                        encoding_str = pop + encoding_str 
                    else:
                        encoding_string.append(encoding_str)
                        break
                count.append(stack.pop(-1))
                if not stack:
                    print(list(reversed(count)))
                    print(list(reversed(encoding_string)))
                    self.printEncoding(list(reversed(count)), list(reversed(encoding_string)))
                    count = []
                    encoding_string = []
            else:
                stack.append(element)
        
    def printEncoding(self, count, encoding_string):
        for i in range(int(count[0])):
            print(encoding_string[0]),
            for j in range(1, len(count)):
                for k in range(int(count[j])):
                    print(encoding_string[j]),


s = Solution()

st = "3[a]2[bc]"
s.decodeString(st)





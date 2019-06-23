class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        totalCookies = sum(s)
        g = sorted(g)
        count = 0
        while totalCookies:
            count = self.findNextSlot(count, g)
            if count != -1:
                g[count% len(g)] -= 1
                count = count + 1
            else: break
            totalCookies -= 1
            print(str(g) + " " +str(totalCookies))
        return g.count(0)

    def findNextSlot(self, count, g):
        original = count
        while count - original < len(g):
            if g[count% len(g)] > 0:
                return count
            count = count + 1
        return -1

s = Solution()
childlen = [10,9,8,7]
cookies =[5,6,7,8]
print(s.findContentChildren(childlen, cookies))
"""
https://leetcode.com/problems/shopping-offers/
"""
from operator import add
from operator import mul
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        totalSum =  sum(list(map(mul, price, needs)))
        print(totalSum)
        
        for i, spe in enumerate(special):
            specialTotal = ""
            items = spe
            j = i

            if not self.isItemMoreThanNeeds(items, needs):
                specialTotal = spe
                while j < len(special):
                    temp = list(map(add, items, special[j]))
                    if not self.isItemMoreThanNeeds(temp, needs):
                        specialTotal = temp
                    j += 1

            if len(specialTotal) != 0:
                tempTotalSum = specialTotal[-1]
                for i in range(len(needs)):
                    short = needs[i] - specialTotal[i]
                    tempTotalSum += short*price[i]
                totalSum = min(tempTotalSum,totalSum)

        return totalSum

    def isItemMoreThanNeeds(self, items, needs):
        for i, need in enumerate(needs):
            if items[i] > need:
                return True
        return False


price = [2,3,4]
special = [[1,1,0,4],[0,0,0,0],[2,2,1,9]]
needs = [1,2,1]


# price = [2,5]
# special = [[3,0,5],[1,2,10]]
# needs = [3,2]

# price = [2,3,4]
# special = [[1,1,0,4],[2,2,1,9]]
# needs = [1,2,1]

# price = [2,5]
# special = [[3,0,5],[1,2,10]]
# needs = [3,2]

s = Solution()
print(s.shoppingOffers(price, special, needs))
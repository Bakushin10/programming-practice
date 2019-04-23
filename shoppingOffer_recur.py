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
        totalSum = sum(list(map(mul, price, needs)))

        for i in range(len(special)):
            # get the combination of specials
            totalSpecial = self.shoppingOfferHelper(i, special, totalSpecial, needs)
            # calculate the sum of totalSpecial
            total = self.getTotal(totalSpecial, needs, price)
            totalSum = min(totalSum, total)
        return totalSum
    
    def shoppingOfferHelper(self, i, special, totalSpecial, needs):
        
        if i == len(special):
            return totalSpecial
        
        addedSpecial = list(map(add, special[i], totalSpecial))
        if not self.isItemMoreThanNeeds(addedSpecial, needs):
            return self.shoppingOfferHelper(i, special, addedSpecial, needs)
        else:
            return self.shoppingOfferHelper(i+1, special, totalSpecial, needs)

    def getTotal(self, totalSpecial, needs, price):
        total = totalSpecial[-1]
        for i in range(len(needs)):
            short = needs[i] - totalSpecial[i]
            total += short*price[i]
        return total

    def isItemMoreThanNeeds(self, items, needs):
        for i, need in enumerate(needs):
            if items[i] > need:
                return True
        return False

price = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
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
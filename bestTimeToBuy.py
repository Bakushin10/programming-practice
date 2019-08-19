
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54131/Well-explained-Python-DP-with-comments
"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k >= len(prices)/2:
            return self.maxProfits(k, prices)

        profits = [0]*len(prices)
        for j in range(k):
            preprofit = 0
            for i in range(1,len(prices)):
                profit = prices[i] - prices[i-1]
                preprofit = max(preprofit+profit, profits[i])
                profits[i] = max(profits[i-1], preprofit)
                print(profits)
        return profits[-1]


    def maxProfits(self, k, prices):
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit


prices = [3,2,6,5,0,3]
k = 2
s = Solution()
s.maxProfit(k, prices)
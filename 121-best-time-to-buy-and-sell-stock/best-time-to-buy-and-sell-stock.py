class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        maxProfit = 0
        while i < len(prices):
            while j < len(prices):
                if (prices[j] - prices[i]) > maxProfit:
                    maxProfit = prices[j] - prices[i]
                elif (prices[j] - prices[i]) < 0:
                    i = j
                j = j + 1
            i = i + 1
        return maxProfit  
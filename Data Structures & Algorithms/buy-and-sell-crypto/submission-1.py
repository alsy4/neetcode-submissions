class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        for i in range(n):
            for j in range(i, n, 1):
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)

        return maxProfit




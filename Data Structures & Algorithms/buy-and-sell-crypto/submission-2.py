class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        left, right = 0, 1

        while right < n: 
            sell = prices[right]
            buy = prices[left]
            if buy < sell:
                profit = sell - buy
                maxProfit = max(maxProfit, profit)
            else:
                left = right

            right += 1

        return maxProfit



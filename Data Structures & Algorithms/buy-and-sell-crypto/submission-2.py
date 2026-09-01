class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy = prices[0]

        for i in range(len(prices) - 1):
            profit = max(profit, prices[i] - buy)
            if prices[i] < buy:
                buy = prices[i]
        profit = max(profit, prices[-1] - buy)
        return profit
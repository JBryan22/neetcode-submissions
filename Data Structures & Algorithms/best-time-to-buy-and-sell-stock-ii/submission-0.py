class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        bought = False
        prevBuyAmt = 0

        for i in range(len(prices)):
            if i == len(prices) - 1:
                if bought:
                    mp += prices[i] - prevBuyAmt
                    bought = False
                break
            if prices[i+1] < prices[i] and bought:
                mp += prices[i] - prevBuyAmt
                prevBuyAmt = 0
                bought = False
            elif prices[i+1] > prices[i] and not bought:
                prevBuyAmt = prices[i]
                bought = True
        return mp
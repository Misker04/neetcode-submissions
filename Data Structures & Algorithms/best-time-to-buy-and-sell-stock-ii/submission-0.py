class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        gmax = 0
        start = prices[0]
        for price in prices:
            if price > start:
                gmax += price - start
            start = price
        return gmax
        
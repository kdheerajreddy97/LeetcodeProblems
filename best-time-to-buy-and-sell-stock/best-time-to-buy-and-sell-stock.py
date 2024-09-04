class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        
        while r < len(prices):
            profit = prices[r] - prices[l]
            res = max(res, profit)
            if profit < 0:
                l = r
            r+=1
        return res
            
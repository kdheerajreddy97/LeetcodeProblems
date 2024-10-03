class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         l = 0
#         r = 0
#         res = 0
        
#         while r < len(prices):
#             profit = prices[r] - prices[l]
#             res = max(res, profit)
#             if profit < 0:
#                 l = r
#             r+=1
#         return res
            
    
        min_profit = prices[0]
        max_profit = 0
        
        for i in range(1,len(prices)):
            profit = prices[i] - min_profit
            
            if profit < 0:
                min_profit = prices[i]
            else:
                max_profit = max(max_profit, profit)
                
        return max_profit
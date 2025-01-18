# Brute force - split the array into 2 halfes and find max profit for each half i.e. calculate max profit till point i, and max profit from i to n
# Single Pass: Time: O(n); Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # Min Buying Price
        buy1 = prices[0]
        # Max Profit1
        sell1 = 0
        # Min Buying price after deducting the sell1(Profit1)
        buy2 = prices[0]
        # Max Total Profit
        sell2 = 0

        for i in range(1, n):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i] - buy1)
            buy2 = min(buy2, prices[i] - sell1)
            sell2 = max(sell2, prices[i] - buy2)

        return sell2
        
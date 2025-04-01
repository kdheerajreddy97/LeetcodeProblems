class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int buy_price = prices[0];
        for(int i = 1; i < prices.length; i++){
            if (buy_price > prices[i]){
                buy_price = prices[i];
            }
            max_profit = Math.max(max_profit, prices[i] - buy_price);
        }

        return max_profit;
    }
}
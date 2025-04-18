class Solution {
    public int maxProfit(int[] prices) {
        int buy1 = prices[0];
        int sell1 = 0; // profit1
        int buy2 = prices[0]; // effective buy in price after removing profit1
        int sell2 = 0; // profit2

        for(int i = 1; i < prices.length; i++){
            buy1 = Math.min(prices[i],buy1);
            sell1 = Math.max(sell1, prices[i] - buy1);
            buy2 = Math.min(buy2, prices[i]-sell1);
            sell2 = Math.max(sell2, prices[i]-buy2);
        }

        return sell2;

    }
}
class Solution {
    public int maxProfit(int k, int[] prices) {
        int[] buy = new int[k+1];
        int[] sell = new int[k+1];

        Arrays.fill(buy,prices[0]);

        for (int i = 1; i< prices.length; i++){
            for(int j =1; j<= k; j++){
                buy[j] = Math.min(buy[j], prices[i]-sell[j-1]);
                sell[j] = Math.max(sell[j], prices[i]-buy[j]);
            }
            
        }
        return sell[k];
    }
}
class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int[] bucket = new int[n+1];

        for(int i =0;i <n; i++){
            if (citations[i] > n) {
                bucket[n] += 1;
            }
            else{
                bucket[citations[i]] += 1;
            }
            
        }
        int count = 0;
        for(int i=n; i >=0; i--){
            count += bucket[i];
            if (count >= i){
                return i;
            }
        }
    return 0;
    }
}
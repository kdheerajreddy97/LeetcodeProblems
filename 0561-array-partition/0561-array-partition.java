class Solution {
    public int arrayPairSum(int[] nums) {
        int n = nums.length;
        HashMap<Integer, Integer> map = new HashMap<>();
        int min_val = nums[0];
        int max_val = nums[0];
        int res = 0;
        //Bucket Sort
        for (int i=0; i < n; i++){
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
            min_val = Math.min(min_val, nums[i]);
            max_val = Math.max(max_val, nums[i]);
        }
        Boolean Flag = false;
        for (int i = min_val; i <= max_val; i++){
            if (map.containsKey(i)){
                if (Flag){
                    map.put(i, map.get(i)-1);
                }
                int freq = map.get(i);
                if (freq % 2 == 0){
                    res += (freq/2) * i;
                    Flag = false; // even
                }
                else{
                    res += (freq-1)/2 * i;
                    res += i;
                    Flag = true; //odd
                }
            }
        }
        return res;
    }
}
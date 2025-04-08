class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        Stack<Integer> mystack = new Stack<>();
        int[] res = new int[n];
        Arrays.fill(res,-1);
        for (int i = 0; i< 2*n; i++){
            while(!mystack.isEmpty() && nums[mystack.peek()] < nums[i%n]){
                int prev_index = mystack.pop();
                res[prev_index] = nums[i%n];
            }
            if (i < n){
                mystack.push(i);
            }
            // else{
            //     if (mystack.peek() == i%n){
            //         break;
            //     }
            // }
            
        }
        return res;
    }
}
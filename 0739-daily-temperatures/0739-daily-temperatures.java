class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        Stack<Integer> myStack = new Stack<>();
        int[] ans = new int[n];

        for(int i =0; i < n; i++){
            while(!myStack.isEmpty() && temperatures[myStack.peek()] < temperatures[i]){
                int previndex = myStack.pop();
                ans[previndex] = i - previndex;
            }
            myStack.push(i);
        }

        return ans;
    }
}
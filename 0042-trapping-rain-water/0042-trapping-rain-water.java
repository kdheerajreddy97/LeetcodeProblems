class Solution {
    public int trap(int[] height) {
        int l = 0;
        int r = height.length-1;
        int max_left = height[l];
        int max_right = height[r];
        int trapped_water = 0;
        while (l < r){
            if (max_left < max_right){
                l += 1;
                max_left = Math.max(max_left, height[l]);
                trapped_water += max_left - height[l];
            }
            else{
                r -= 1;
                max_right = Math.max(max_right, height[r]);
                trapped_water += max_right - height[r];
            }
        }
        return trapped_water;

    }
}
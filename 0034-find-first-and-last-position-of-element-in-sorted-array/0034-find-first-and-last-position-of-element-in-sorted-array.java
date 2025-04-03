class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        int left  = binarysearch(nums, target, true);
        int right = binarysearch(nums, target, false);
        int[] res = {left,right};
        return res;
    }

    public int binarysearch(int[] nums, int target, Boolean findleft){
        int l = 0;
        int r = nums.length-1;
        int index = -1;
        while (l <= r){
            int mid = l + (r-l)/2;

            if (nums[mid] > target){
                r = mid - 1;
            }
            else if (nums[mid] < target){
                l = mid + 1;
            }
            else{
                index = mid;
                if (findleft){
                    r = mid - 1;
                }
                else{
                    l = mid + 1;
                }
            }
        }
    return index;
    }
}
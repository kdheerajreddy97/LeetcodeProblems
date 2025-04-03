class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        int top = 0;
        int bottom = m-1;
        int left = 0;
        int right = n-1;
        int row = -1;
        while (top <= bottom){
            int mid = top + (bottom - top) / 2;

            if (matrix[mid][0] > target){
                bottom = mid - 1;
            }
            else if (matrix[mid][n-1] < target){
                top = mid + 1;
            }
            else{
                row = mid;
                break;
            }

        }

        if (row == -1) {
            return false;
        }

        while (left <= right){
            int mid2 = left + (right-left)/2;

            if (matrix[row][mid2] == target){
                return true;
            }
            else if (matrix[row][mid2] > target){
                right = mid2 - 1;
            }
            else{
                left = mid2 + 1;
            } 
        }

        return false;

    }
}
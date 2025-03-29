class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[] res = new int[m*n];
        int r = 0;
        int c = 0;
        boolean dir = true;
        for (int i =0; i < m*n; i++){
            res[i] = mat[r][c];

            if (dir){
                if (c == n-1){
                    r += 1;
                    dir = false;
                }
                else if (r == 0){
                    c += 1;
                    dir = false;
                }
                else{
                    r -= 1;
                    c += 1;
                }
            }

            else{
                if (r == m-1){
                    c += 1;
                    dir = true;
                }
                else if (c == 0){
                    r += 1;
                    dir = true;
                }
                else{
                    r += 1;
                    c -= 1;
                }
            }
            
        }
        return res;
    }
}
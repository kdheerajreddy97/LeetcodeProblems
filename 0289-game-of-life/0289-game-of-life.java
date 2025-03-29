class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;

        for(int i =0; i < m; i++){
            for (int j = 0; j < n; j++){
                int nei = neighbours(i,j,m,n,board);
                if (board[i][j] == 0){
                    if (nei == 3){
                        board[i][j] = 3; // live == 1
                    }
                }
                if (board[i][j] == 1){
                    if (nei != 2 && nei != 3){
                        board[i][j] = 2; // dead == 0
                    }
                }
            }
        }

        for(int i =0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (board[i][j] == 3){
                    board[i][j] = 1;
                }
                if (board[i][j] == 2){
                    board[i][j] = 0;
                }
            }
        }
    }

    public int neighbours(int r, int c, int m, int n, int[][] board){
        int[][] dir = {{0,-1}, {0,1},{1,0},{-1,0},{1,-1},{-1,1},{1,1},{-1,-1}};
        int nei = 0;
        for(int i =0; i< dir.length; i++){
            int r1 = r + dir[i][0];
            int c1 = c + dir[i][1];

            if (r1>=0 && r1<m && c1>=0 && c1<n && (board[r1][c1] == 1 || board[r1][c1] == 2)){
                nei += 1;
            }
        }
        return nei;
    }
}
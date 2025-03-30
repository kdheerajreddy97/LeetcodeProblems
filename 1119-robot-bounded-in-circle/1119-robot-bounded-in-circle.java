class Solution {
    public boolean isRobotBounded(String instructions) {
        int[][] directions = {{0,1},{1,0},{0,-1},{-1,0}};
        int x = 0;
        int y = 0;
        int idx = 0;
        for (int i = 0; i < instructions.length(); i++){
            if (instructions.charAt(i) == 'G'){
                int[] dir = directions[idx];
                x += dir[0];
                y += dir[1];
            }
            else if(instructions.charAt(i) == 'L'){
                idx = (idx + 1) % 4;
            }
            else{
                idx = (idx + 3) % 4;
            }
        }

        if ((x == 0 & y == 0) || idx != 0){
            return true;
        }
        else{
            return false;
        }
    }
}
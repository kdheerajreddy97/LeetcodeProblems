class Solution {
    public int shortestWordDistance(String[] wordsDict, String word1, String word2) {
      int p1 = -1;
      int p2 = -1;
      int dist = Integer.MAX_VALUE;

      for (int i = 0; i< wordsDict.length; i++){
        if (wordsDict[i].equals(word1)){
            if (wordsDict[i].equals(word2)){
                if (p1<p2){
                    p1 = i;
                }
                else{
                    p2 = i;
                }
            }
            else{
                p1 = i;
            }
        }

        else if (wordsDict[i].equals(word2)){
            p2 = i;
        }
        

        if (p1 != -1 & p2 != -1){
            dist = Math.min(dist, Math.abs(p1-p2));
        }
      } 
      return dist;
    }
}
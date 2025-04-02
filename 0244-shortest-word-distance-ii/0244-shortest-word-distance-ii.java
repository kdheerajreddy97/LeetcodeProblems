class WordDistance {
    HashMap<String, ArrayList<Integer>> map = new HashMap();

    public WordDistance(String[] wordsDict) {
        for (int i =0; i < wordsDict.length; i++){
            if (!map.containsKey(wordsDict[i])){
                map.put(wordsDict[i], new ArrayList<Integer>());
            }
            map.get(wordsDict[i]).add(i);
        }
    }
    
    public int shortest(String word1, String word2) {
        ArrayList<Integer> list1 = map.get(word1);
        ArrayList<Integer> list2 = map.get(word2);

        int p1 = 0;
        int p2 = 0;
        int m = list1.size();// Arraylist so .size
        int n = list2.size();
        int min_dist = Integer.MAX_VALUE;
        while (p1 < m && p2 < n){
            if (list1.get(p1)<list2.get(p2)){ // Arraylist so .get
                min_dist = Math.min(min_dist, list2.get(p2)-list1.get(p1));
                p1++;
            }
            else{
                min_dist = Math.min(min_dist, list1.get(p1)-list2.get(p2));
                p2++;
            }
        }
        return min_dist;

    }
}

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance obj = new WordDistance(wordsDict);
 * int param_1 = obj.shortest(word1,word2);
 */
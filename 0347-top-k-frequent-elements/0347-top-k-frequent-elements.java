class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums){
            map.put(num, map.getOrDefault(num,0)+1);
        }
        PriorityQueue<Map.Entry<Integer,Integer>> heap = new PriorityQueue<>(Comparator.comparingInt(Map.Entry::getValue));
        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            heap.offer(entry);
            if (heap.size() > k){
                heap.poll();
            }
        }

        int[] result = new int[k];

        for(int i=0; i < k; i++){
            result[i] = heap.poll().getKey();
        }
        return result;

    }
}
// MinHeap: Time: O(Nlogk); Space: O(k)
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int num:nums){
            heap.offer(num);

            if (heap.size() > k){
                heap.poll();
            }
        }

        return heap.peek();
    }
}

// MaxHeap: Time: O(N) + O(klogN); Space: O(N)
// class Solution {
//     public int findKthLargest(int[] nums, int k) {
//         PriorityQueue<Integer> max_heap = new PriorityQueue<>(Collections.reverseOrder());
//         for(int num:nums){
//             max_heap.offer(num);
//         }

//         for(int i=0; i < k-1; i++){
//             max_heap.poll();
//         }

//         return max_heap.peek();
//     }
// }
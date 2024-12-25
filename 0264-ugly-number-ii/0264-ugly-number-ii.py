# Exhaustive tree; using min-heap and hashset
# I forgot the heap function while solving this problem make sure to remember next time
# Time: O(n*logN); Space: O(N) + O(N)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = []
        ugly_numbers = set()
        curr_ugly = 1
        ugly_numbers.add(curr_ugly)
        heapq.heappush(min_heap, 1)
        prime = [2,3,5]

        for _ in range(n):
            curr_ugly = heapq.heappop(min_heap)
            for num in prime:
                temp = num * curr_ugly
                if temp not in ugly_numbers:
                    heapq.heappush(min_heap, temp)
                    ugly_numbers.add(temp)
        
        return curr_ugly

        
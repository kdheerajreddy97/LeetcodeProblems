class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dict = {}
        max_val = -1
        for num in nums:
            k = self.sum_of_digits(num)
            if k in dict:
                heapq.heappush(dict[k],num)
            else:
                dict[k] = []
                heapq.heappush(dict[k],num)    
        for key, min_heap in dict.items():
            while len(min_heap) > 2:
                heapq.heappop(min_heap)
            if len(min_heap) == 2:
                max_val = max(max_val, sum(min_heap))
        return max_val

    
    def sum_of_digits(self, num):
        sum = 0
        digit = 0
        while num > 0:
            digit = num % 10
            num = num // 10
            sum += digit
        return sum

    

        
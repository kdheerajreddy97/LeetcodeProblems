class Solution:
    def feasible(self, capacity, weights, days):
        ndays = 1
        temp = capacity
        for weight in weights:
            if temp < weight:
                ndays += 1
                temp = capacity
            temp -= weight
        return ndays <= days

    def splitArray(self, nums: List[int], k: int) -> int:
        # Find min and max
        min = 0
        max = 0

        for weight in nums:
            if min < weight:
                min = weight
            max += weight
        l = min
        r = max
        # Apply binary search over this min to max array, For each value of binary check how many days its taking and increment pointer according to that 
        while l < r:
            mid  = (l + r) // 2
            if self.feasible(mid, nums, k):
                r = mid
            else:
                l = mid + 1
        # Contunie till you get the least
        return l
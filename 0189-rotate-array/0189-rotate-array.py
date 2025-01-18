class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n
        if n ==1:
            return nums
        self.reverse(0, n, nums)
        self.reverse(0,k,nums)
        self.reverse(k, n, nums)

    def reverse(self, i,j, nums):
        l = i
        r = j-1
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1


    # def swap(self, arr):
    #     l = 0
    #     r = len(arr)-1
    #     while l < r:
    #         temp = arr[l]
    #         arr[l] = arr[r]
    #         arr[r] = temp
    #         l += 1
    #         r -= 1
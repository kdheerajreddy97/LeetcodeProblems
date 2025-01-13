class Solution:
    def reverseBits(self, n: int) -> int:
        power = 31
        res = 0
        while n:
            # Get the least significant digit and send it to 31st position
            # << left shift
            res += (n & 1) << power
            # decrement he power
            power -= 1
            # remove the lsd
            n = n >> 1
        return res
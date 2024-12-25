# Approach1: Repeated Subraction of divisor from dividend
# Approach2: Bitwise shift
# Time: O(logN); Space: O(1)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Define the 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle edge cases
        if divisor == 0:
            raise ValueError("Division by zero is not allowed.")
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  # Prevent overflow
            
        result = 0

        ldividend = abs(dividend)
        ldivisor = abs(divisor)

        while ldividend >= ldivisor:
            numShifts = 1

            while (ldivisor << numShifts) <= ldividend:
                numShifts += 1

            numShifts -= 1

            result += 1 << numShifts

            ldividend = ldividend - (ldivisor << numShifts)

        
        if dividend < 0 and divisor < 0: return result
        elif dividend < 0 or divisor < 0: return -result
        return result

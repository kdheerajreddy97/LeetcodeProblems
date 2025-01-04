# Approach1: BFS with Memiozation - Since minimum number of steps this is more optimized
# Approach2: DFS - Its complicated as there might repeated sub prolems which goes into cycle
# Approach3: Greedy - Best approach; If even /2 else + 1 until value is greater than target
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while target > startValue:
            if target % 2 == 0:
                target = target // 2
            else:
                target = target + 1
            count += 1
        
        return count + ( startValue - target)

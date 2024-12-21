# 2 Conditions to be successfull
# 1. If after one cycle if it faces north it always faces north(Can be any direction N|S|E|W) - fails always - so it works when it doesn't point to same direction
# 2. After once cycle if its visits origin again then its True
# Time: O(n); Space: O(1)
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
                    # North, East, South, West
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        idx = 0
        x = 0
        y = 0

        for step in instructions:
            # If 'G' - add the current pointer value to current x and y
            if step == 'G':
               dr, dc = directions[idx]
               x += dr
               y += dc
            # 3 steps clockwise rotation
            elif step == 'L':
                idx = (idx + 3) % 4
            # 1 step clockwise rotation
            else:
                idx = (idx + 1) % 4
        # Condition 1 and 2 as discussed in the top
        # idx != 0 - This is because at any of 4 iterations from here it will reach a cycle
        if (x == 0 and y == 0) or idx != 0:
            return True
        else:
            return False

        
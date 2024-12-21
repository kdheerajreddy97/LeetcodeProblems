# 2 Conditions to be successfull
# 1. If after one cycle if it faces north it always faces north(Can be any direction N|S|E|W) - fails always - so it works when it doesn't point to same direction
# 2. After once cycle if its visits origin again then its True
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
                    # North, East, South, West
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        idx = 0
        x = 0
        y = 0


        for step in instructions:
            if step == 'G':
               dr, dc = directions[idx]
               x += dr
               y += dc
            elif step == 'L':
                idx = (idx + 3) % 4
            else:
                idx = (idx + 1) % 4
            
        if (x == 0 and y == 0) or idx != 0:
            return True
        else:
            return False

        
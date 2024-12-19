# Approach: Greedy
# Time: 2 Pass - O(n); Space: O(1)
class Solution:
    # Find the potential target
    def findpotential(self, tops, bottoms, target):
        top_rotate = 0
        bottom_rotate = 0
        for i in range(len(tops)):
            # if any one tile(2 numbers) doesn't match that means it cannot be done
            if tops[i] != target and bottoms[i] != target:
                return float('inf')
            # calc tops rotations
            elif tops[i] != target:
                top_rotate += 1
            # calc bottom rotations
            elif bottoms[i] != target:
                bottom_rotate += 1
        # return min of both
        return min(top_rotate, bottom_rotate)

    # Find min rotations
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        # Max of only 2 potential targets will be there, so we can return anyone out of it
        top = self.findpotential(tops, bottoms, tops[0])
        bottom = self.findpotential(tops, bottoms, bottoms[0])
        res = min(top,bottom)

        if res != float('inf'):
            return res
        else:
            return -1

        


            



        
                
                    

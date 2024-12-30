class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dict = {}

        for i, val in enumerate(arr):
            if val in dict:
                dict[val] += 1
            else:
                dict[val] = 1
        
        for i, val in enumerate(target):
            if val in dict and dict[val] != 0:
                dict[val] -= 1
            else:
                return False
        
        if sum(dict.values()) == 0:
            return True
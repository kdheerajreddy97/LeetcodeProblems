# Approach: Greedy; Time: O(s) + O(t*logk); Space: O(s)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s = len(source)
        t = len(target)
        pos = {}
        # Fil the dictionary containing the all the source string positons
        for i in range(s):
            if source[i] in pos:
                pos[source[i]].append(i)
            else:
                pos[source[i]]= [i]
        

        source_pointer = -1
        subsequences = 1
        for i in range(t):
            char = target[i]
            if char not in pos:
                return -1
            # Binary search to find the next higest position to the source_pointer
            next_match_pos = self.binarysearch(pos[char], source_pointer)
            # Increase the subsequences as it didnt not find any matching character
            if next_match_pos == -1:
                subsequences += 1
                source_pointer = pos[char][0]
            else:
            # Matching found do update the source pointer
                source_pointer = next_match_pos
        return subsequences
        

    def binarysearch(self, arr, target):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > target:
                r = r-1
            else:
                l = l+1
        if l < len(arr):
            return arr[l]
        else:
            return -1




        
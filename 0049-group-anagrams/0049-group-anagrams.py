class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for c in string:
                pos = ord(c) - ord('a')
                arr[pos] += 1
            anagrams[tuple(arr)].append(string)
        
        return list(anagrams.values())
        
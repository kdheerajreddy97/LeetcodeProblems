class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         dict = {}
        
        
#         for s in strs:
#             key = sorted(s)
#             key = ''.join(key)
#             if key in dict:
#                 dict[key].append(s)
#             else:
#                 dict[key] = [s]
#         return dict.values()
            
                
        anagrams = defaultdict(list)
        
        for str in strs:
            arr = [0] * 26
            for s in str:
                pos = ord(s) - ord('a')
                arr[pos] += 1
            anagrams[tuple(arr)].append(str)
        return anagrams.values()
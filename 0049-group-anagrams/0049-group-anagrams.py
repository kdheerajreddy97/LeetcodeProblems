class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        
        
        for s in strs:
            key = sorted(s)
            key = ''.join(key)
            if key in dict:
                dict[key].append(s)
            else:
                dict[key] = [s]
        return dict.values()
            
                
        
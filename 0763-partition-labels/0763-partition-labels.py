class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_count = {}
        res = []
        for i in range(len(s)):
            last_count[s[i]] = i
        print(last_count)
        
        end = 0
        start = 0
        for i in range(len(s)):
            end = max(end, last_count[s[i]])
            
            
            if i == end:
                length = (end - start + 1)
                res.append(length)
                start = i + 1
        return res
            
            
            
            
            
            
            
            
            
            
        
        
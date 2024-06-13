class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = defaultdict(list)
        for index, char in enumerate(s):
            my_dict[char].append(index)
        
        for key, values in my_dict.items():
                if len(values) == 1:
                    return values[0]
        return -1
                
            
        
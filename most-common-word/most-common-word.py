class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph_lower = paragraph.lower()
        paragraph_lower = re.sub(r"[^\w\s]", ' ', paragraph_lower)
        paragraph_array = paragraph_lower.split()
        my_dict = {}
        max_value = float('-inf')
        max_key = ""
        for word in paragraph_array:
            if (word in my_dict):
                my_dict[word] += 1
            else:
                my_dict[word] = 1
                
        for key, value in my_dict.items():
            if (value > max_value) and (key not in banned):
                max_value = value
                max_key = key
        return max_key
                
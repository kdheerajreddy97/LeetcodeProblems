#Space Complexity: O(1) ; Time Complexity: O(1)
class Solution:
    
        def __init__(self):
            self.thousand = ["", " Thousand ", " Million ", " Billion "]
            self.below20 = [" ", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                  "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            self. tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        
        def numberToWords(self, num: int) -> str: 
            result = ""
            if num == 0:
                return "Zero"
            i = 0
            
            while num > 0:
                triplet =  num % 1000
                if triplet > 0:
                    result = self.helper(triplet).strip() + self.thousand[i] + result
                i += 1
                num = num // 1000
                    
            return result.strip()
            
            
            
            
        
        def helper(self, num: int) -> str:
            if num < 20:
                return self.below20[num]
            
            elif num < 100:
                return self.tens[num//10] + " " + self.below20[num % 10]
    
            else:
                return self.below20[num//100] + " Hundred " + self.helper(num % 100)
        
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        
        for i in range(numRows -1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(1,len(temp)):
                sum = temp[j] + temp[j-1]
                row.append(sum)
            res.append(row)
        return res
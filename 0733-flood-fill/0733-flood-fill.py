class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows = len(image)
        columns = len(image[0])
        
        starting_pixel = image[sr][sc]
        
        if starting_pixel == color:
            return image
        
        
        def dfs(sr,sc):
            
            if sr < 0 or sr >= rows or sc < 0 or sc >= columns or image[sr][sc]!= starting_pixel:
                return
            
            image[sr][sc] = color
            directions = [[-1,0],[0,1],[1,0],[0,-1]]
            
            
            for dr, dc in directions:
                    dfs(sr+dr,sc+dc)
                
        dfs(sr,sc)
        return image
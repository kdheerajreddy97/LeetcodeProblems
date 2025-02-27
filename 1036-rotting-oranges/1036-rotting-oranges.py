class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
 
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                for dir in directions:
                    nr = curr[0] + dir[0]
                    nc = curr[1] + dir[1]

                    if (nr >= 0 and nc >= 0 and nr < m and nc < n and (grid[nr][nc] == 1)):
                        grid[nr][nc] = 2 # Mark this rotten
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
        
        if fresh == 0:
            return time - 1
        else:
            return -1




        
# Approach: BFS ; Time: O(m*n); Space: O(m*n)
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         q = deque()
#         fresh = 0
#         time = 0
#         directions = [(0,1),(1,0),(-1,0),(0,-1)]
#         # Add the rotten oranges to the queue and keep the fresh oranges count
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 2:
#                     q.append((i,j))
#                 elif grid[i][j] == 1:
#                     fresh += 1
        
#         if fresh == 0:
#             return 0
#         # Level order traversal
#         while q:
#             for i in range(len(q)):
#                 curr = q.popleft()
#                 for dir in directions:
#                     nr = curr[0] + dir[0]
#                     nc = curr[1] + dir[1]

#                     if (nr >= 0 and nc >= 0 and nr < m and nc < n and (grid[nr][nc] == 1)):
#                         grid[nr][nc] = 2 # Mark this rotten
#                         q.append((nr,nc))
#                         fresh -= 1
#             time += 1
        
#         if fresh == 0:
#             return time - 1
#         else:
#             return -1


# Approach: DFS ; Time: O(m2*n2); Space: O(m*n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 2
        m = len(grid)
        n = len(grid[0])
        min_minutes = time
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    self.dfs(i, j, grid, time)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                min_minutes = max(grid[i][j] , min_minutes)
        return min_minutes - 2
    
    def dfs(self, i, j, grid, time):
        m = len(grid)
        n = len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        # Base case 
        if i < 0 or j < 0 or i >= m or j >= n:
            return
        if grid[i][j] != 1 and grid[i][j] < time:
            return
        # Logic
        grid[i][j] = time
        for dir in directions:
            nr = i + dir[0]
            nc = j + dir[1]
            self.dfs(nr, nc, grid, time + 1)



                

        
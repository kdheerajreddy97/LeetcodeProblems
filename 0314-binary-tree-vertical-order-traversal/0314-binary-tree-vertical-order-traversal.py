# 2 approaches BFS and DFS: BFS is easier than DFS; Start from 0 if left -1 if right +1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Approach 1: BFS
# Time Complexity: O(N); Space Complexity: O(N)
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = defaultdict(list)
        index = 0
        if not root:
            return []
        q = deque()
        q.append([root,0])
        dict[0].append(root.val)
        min_index = 0
        max_index = 0
        res = []
        # level order traversal
        while q:
                [node, i] = q.popleft()
                if node.left:
                    a = i - 1
                    q.append([node.left,a])
                    dict[a].append(node.left.val)
                    min_index = min(a, min_index)
                if node.right:
                    b = i + 1
                    q.append([node.right,b])
                    dict[b].append(node.right.val)
                    max_index = max(b, max_index)
        # Bucket Sort
        for i in range(min_index, max_index + 1):
            res.append(dict[i])
        return res

# Approach 2: DFS; 
# Time Complexity: O(N)(DFS)+O(N)(inserts)+O(NlogN)(sorting)=O(NlogN); Space Complexity: O(N)
# class Solution:
#     def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []
#         if not root:
#             return []
#         dict = defaultdict(list)
#         self.min_col = 0
#         self.max_col = 0

#         def dfs(node, row, col):
#             # Base case
#             if not node:
#                 return
#             # Add to dict list of row, node pairs
#             dict[col].append([row,node.val])
#             # Update min and max
#             self.min_col = min(col, self.min_col)
#             self.max_col = max(col, self.max_col)
#             # Recurse
#             dfs(node.left, row + 1, col - 1)
#             dfs(node.right, row + 1, col + 1)

#         dfs(root,0,0)

#         # Bucket Sort
#         for i in range(self.min_col, self.max_col + 1):
#             temp = []
#             row_nodes = dict[i]
#             row_nodes = sorted(row_nodes, key = lambda x: x[0])
#             for row, node in row_nodes:
#                 temp.append(node)
#             res.append(temp)
#         return res



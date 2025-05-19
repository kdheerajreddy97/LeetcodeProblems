# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Approach1: BFS level order traversal: Time: O(N); Space: O(N)
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = deque([root])
        sum = 0
        while q:
                node = q.popleft()
                if low <= node.val <= high:
                    sum += node.val
                # Igoring sub trees not following this condition
                if node.val > low and node.left:
                    q.append(node.left)
                if node.val < high and node.right:
                    q.append(node.right)
        return sum

# Approach1: DFS Preorder or Postorder or Inorder: Time: O(N); Space: O(N)
# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         def dfs(node):
#             total_sum = 0
#             if not node:
#                  return 0
#             if low <= node.val <= high:
#                 total_sum += node.val
            
#             if node.val > low:
#                 total_sum += dfs(node.left)
#             if node.val < high:
#                 total_sum += dfs(node.right)
            
#             return total_sum
        
#         return dfs(root)
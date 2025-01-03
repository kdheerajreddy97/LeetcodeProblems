# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time: O(n); Space:O(1)
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def dfs(node):
            # Base Case:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.moves += abs(left) + abs(right)

            return left + right + node.val - 1

        dfs(root)
        return self.moves
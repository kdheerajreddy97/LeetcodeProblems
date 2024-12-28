# 2 approaches BFS and DFS: BFS is easier than DFS; Start from 0 if left -1 if right +1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = defaultdict(list)
        index = 0
        if not root:
            return []
        q = deque([[root,0]])
        dict[0].append(root.val)
        min_index = 0
        max_index = 0
        res = []
        # level order traversal
        while q:
            for i in range(len(q)):
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
        
        
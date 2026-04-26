# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        res = [0]
        def dfs(root):
            if not root:
                return 0
            depth = max(1 + dfs(root.left), 1 + dfs(root.right))
            res[0] = max(res[0], depth)
            return depth
        
        dfs(root)
        return res[0]
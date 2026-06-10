# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.curClosest = 0
        self.minDif = float("inf")

        def dfs(node):
            if not node:
                return

            dif = abs(node.val - target)
            if dif < self.minDif:
                self.curClosest = node.val
                self.minDif = dif

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.curClosest
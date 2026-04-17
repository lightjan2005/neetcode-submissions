# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
 
        def dfs(node, maxVal, count):
            if not node:
                return count

            if node.val >= maxVal:
                count += 1
                maxVal = node.val

            count = dfs(node.left, maxVal, count)
            count = dfs(node.right, maxVal, count)
            return count

        return dfs(root, float("-inf"), 0)
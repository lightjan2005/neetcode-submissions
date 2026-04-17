# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # put root and also the cur max and cur min
        queue = deque([[root, float("-inf"), float("inf")]])

        while queue:
            current, left, right = queue.popleft()
            if not (left < current.val < right):
                return False
            if current.left:
                queue.append([current.left, left, current.val])
            if current.right:
                queue.append([current.right, current.val, right])

        return True
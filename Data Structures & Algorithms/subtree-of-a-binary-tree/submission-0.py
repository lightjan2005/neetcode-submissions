# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root and not root2:
                return True
            elif not root or not root2:
                return False
            elif root.val != root2.val:
                return False
            
            return isSameTree(root.left, root2.left) and isSameTree(root.right, root2.right)

        if not root:
            return False
        
        if isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
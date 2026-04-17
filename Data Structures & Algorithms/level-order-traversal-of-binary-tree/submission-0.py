# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])

        while queue:
            levelAns = []
            numOfNodes = len(queue)
            for i in range(numOfNodes):
                current = queue.popleft()
                levelAns.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            ans.append(levelAns)
        
        return ans
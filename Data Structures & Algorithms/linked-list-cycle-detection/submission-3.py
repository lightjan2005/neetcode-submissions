# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curNode = head
        fastNode = head

        while fastNode and fastNode.next and fastNode.next.next:
            curNode = curNode.next
            fastNode = fastNode.next.next
            if curNode == fastNode:
                return True
        
        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        cur = head
        fastNode = head

        while fastNode and fastNode.next:
            cur = cur.next
            fastNode = fastNode.next.next
            if cur == fastNode:
                return True

        return False

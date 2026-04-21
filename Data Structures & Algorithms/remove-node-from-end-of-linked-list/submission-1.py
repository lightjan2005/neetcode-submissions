# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        nthFromBeg = length - n
        if nthFromBeg == 0:
            return head.next

        cur = head
        index = 0
        prev = None
        while cur:
            if index == nthFromBeg:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
            index += 1

        return head
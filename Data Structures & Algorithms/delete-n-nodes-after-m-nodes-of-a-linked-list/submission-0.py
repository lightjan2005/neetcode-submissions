# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        count = 0
        cur = head
        skip = n
        while cur:
            count += 1
            if count == m:
                tmp = cur
                while tmp and skip > 0:
                    tmp = tmp.next
                    skip -= 1
                if tmp:
                    cur.next = tmp.next
                    cur = tmp.next
                else:
                    cur.next = None
                    cur = None
                skip = n
                count = 0
            else:
                cur = cur.next

        return head
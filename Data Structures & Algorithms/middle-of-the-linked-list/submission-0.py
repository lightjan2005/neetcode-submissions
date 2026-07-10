# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        l = 0
        cur = head
        r = 0
        while cur:
            cur = cur.next
            r += 1

        midLength = r//2
        ansNode = head
        while ansNode and l < midLength:
            ansNode = ansNode.next
            l += 1

        return ansNode
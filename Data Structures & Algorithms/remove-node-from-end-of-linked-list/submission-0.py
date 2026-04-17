# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curNode = head
        length = 0
        while curNode:
            length += 1
            curNode = curNode.next

        nFromBeg = length - n
        if nFromBeg == 0:
            return head.next

        curNode = head
        index = 0
        prev = None
        while curNode:
            if index == nFromBeg:
                prev.next = curNode.next
                break
            prev = curNode
            curNode = curNode.next
            index += 1
        
        return head
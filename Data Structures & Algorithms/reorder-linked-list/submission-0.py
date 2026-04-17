# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curNode = head
        fastNode = head

        while fastNode and fastNode.next:
            curNode = curNode.next
            fastNode = fastNode.next.next
        
        second = curNode.next
        curNode.next = None

        # Now curNode will be the head of the right linked list
        # Reverse the right linked list
        prev = None
        curNode = second

        while curNode:
            tmp = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = tmp
        
        # merge both linked lists
        first = head

        while prev:
            tmp = first.next
            tmp2 = prev.next
            first.next = prev
            prev.next = tmp
            first = tmp
            prev = tmp2
            

        


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = l1
        head2 = l2
        ans = ListNode()
        head3 = ans
        carry = 0
        while head1 and head2:
            valSum = head1.val + head2.val + carry
            carry = 1 if valSum >= 10 else 0
            head3.val = valSum % 10
            
            if head1.next or head2.next or carry == 1:
                head3.next = ListNode()
            head1, head2, head3 = head1.next, head2.next, head3.next

        while head1:
            valSum = head1.val + carry
            carry = 1 if valSum >= 10 else 0
            head3.val = valSum % 10
            if head1.next or carry == 1:
                head3.next = ListNode()
            head1 = head1.next
            head3 = head3.next
        while head2:
            valSum = head2.val + carry
            carry = 1 if valSum >= 10 else 0
            head3.val = valSum % 10
            if head2.next or carry == 1:
                head3.next = ListNode()
            head2 = head2.next
            head3 = head3.next
        
        if carry == 1:
            head3.val = 1

        return ans
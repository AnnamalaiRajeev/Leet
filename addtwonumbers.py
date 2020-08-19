# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def Listlength(self, head):
        count = 1
        while head.next:
            head = head.next
            count += 1
        return count

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l3 = ListNode()
        # firgure the lengths of the listNodes
        n = max(self.Listlength(l1), self.Listlength(l2))
        head = l3
        for i in range(1, n + 1):
            if l1 == None:
                digit_l1 = 0
            else:
                digit_l1 = l1.val
                l1 = l1.next
            if l2 == None:
                digit_l2 = 0
            else:
                digit_l2 = l2.val
                l2 = l2.next
            _sum = digit_l2 + digit_l1 + carry
            print(_sum)
            if _sum >= 10:
                head.next = ListNode(_sum - 10)
                head = head.next
                carry = 1
            else:
                head.next = ListNode(_sum)
                head = head.next
                carry = 0
        if carry == 1:
            head.next = ListNode(1)
        return l3.next
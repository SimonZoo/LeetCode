# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        t = l3
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            t.val = a+b
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            if l1 or l2:
                t.next = ListNode(0)
                t = t.next
        check = l3
        while check:
            if check.val >= 10:
                check.val -= 10
                if check.next:
                    check.next.val += 1
                else:
                    check.next = ListNode(1)
            check = check.next
        return l3

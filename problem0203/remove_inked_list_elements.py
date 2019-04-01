# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        cur = head
        while cur != None:
            if cur.val is val and prev is None:
                cur = cur.next
                head = head.next
            elif cur.val is val:
                prev.next = cur.next
                cur = cur.next
            elif cur.val is not val:
                prev = cur
                cur = cur.next
        return head
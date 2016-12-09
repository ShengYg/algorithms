# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        if not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre, first, second = dummy, dummy.next, dummy.next.next
        while second:
            first.next = second.next
            second.next = pre.next
            pre.next = second
            second = first.next
        return dummy.next

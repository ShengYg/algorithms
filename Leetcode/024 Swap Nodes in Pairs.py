# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        x = y = head
        if head.next:
            y = y.next
            x.next = y.next
            y.next = x
            head = y
            y = x.next
        while y and y.next:
            x.next = y.next
            y.next = x.next.next
            x.next.next = y
            x = y
            y = y.next
        return head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        nhead, tail, len = head, head, 1
        while tail.next:
            tail = tail.next
            len += 1
        tail.next = head
        k = k % len
        if k:
            for i in range(len - k):
                tail = tail.next
        nhead = tail.next
        tail.next = None
        return nhead

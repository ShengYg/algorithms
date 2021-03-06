# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        fakehead = ListNode(0)
        fakehead.next = head
        pre, cur = fakehead, fakehead
        while cur.next:
            cur = cur.next
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next != cur:
                pre.next = cur
            pre = cur
        return fakehead.next

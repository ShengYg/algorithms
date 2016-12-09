# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return
        fakehead = ListNode(0)
        fakehead.next = head
        cur, flag = fakehead, None
        while cur.next:
            if not flag and cur.next.val >= x:
                flag = cur
            cur = cur.next
            if flag and cur.val < x:
                a = cur.next
                cur.next = flag.next
                flag.next = cur
                while cur.next != flag.next:
                    cur = cur.next
                cur.next = a
                flag = flag.next
        return fakehead.next

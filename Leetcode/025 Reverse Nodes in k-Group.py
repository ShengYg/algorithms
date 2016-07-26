# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        i = j = l = start
        while i.next:
            num, p = k, l
            while p.next and num:
                num -= 1
                p = p.next
            if num > 0:
                return start.next
            i = j = i.next
            count = 0
            while count < k - 1 and l.next.next:
                j = l.next.next
                if j:
                    l.next.next = j.next
                j.next = i
                i = j
                count += 1
            i = l.next
            l.next = j
            j = l = i
        return start.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        a = head
        while l1 or l2:
            if not l1:
                a.next = l2
                a = l2
                l2 = l2.next
            elif not l2:
                a.next = l1
                a = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    a.next = l1
                    a = l1
                    l1 = l1.next
                else:
                    a.next = l2
                    a = l2
                    l2 = l2.next
        return head.next

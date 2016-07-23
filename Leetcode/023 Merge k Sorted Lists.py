import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        heap = []
        nodemap = {}
        head = result = ListNode(0)
        for i in range(len(lists)):
            if lists[i]:
                num = lists[i].val
                lists[i] = lists[i].next
                heap.append(num)
                nodemap[num] = nodemap.get(num, []) + [i]
        heapq.heapify(heap)

        while len(heap) > 1:
            num = heapq.heappop(heap)
            result.next = ListNode(num)
            result = result.next
            i = nodemap[num].pop()
            if lists[i]:
                heapq.heappush(heap, lists[i].val)
                nodemap[lists[i].val] = nodemap.get(lists[i].val, []) + [i]
                lists[i] = lists[i].next
        if not heap:
            return []
        num = heapq.heappop(heap)
        result.next = ListNode(num)
        result = result.next
        result.next = lists[nodemap[num].pop()]
        return head.next
        result.next = lists[nodemap[num].pop()]
        return head.next

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
            node = lists[i]
            if node:
                num = node.val
                node = node.next
                heap.append(num)
                nodemap[num] = nodemap.get(num, []) + [i]
        heapq.heapify(heap)

        while len(heap) > 1:
            num = heapq.heappop(heap)
            result.next = ListNode(num)
            result = result.next
            i = nodemap[num].pop()
            node = lists[i]
            if node:
                heapq.heappush(heap, node.val)
                nodemap[node.val] = nodemap.get(node.val, []) + [i]
                node = node.next
        if not heap:
            return []
        num = heapq.heappop(heap)
        result.next = ListNode(num)
        result = result.next
        result.next = lists[nodemap[num].pop()]
        return head.next

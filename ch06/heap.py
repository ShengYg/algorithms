#heap
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

heapq.heapify(nums)

def heapsort(iter):
	h = []
	for value in iter:
		heappush(h, value)
	return [heappop(h) for i in range(len(h))]

#Queue
from Queue import Queue
from Queue import PriorityQueue
q = Queue()
pq = PriorityQueue()
q.put(3)
q.get(1)
q.empty()
q.full()
q.qsize()

#deque
from collections import deque
d = deque()
d.append('abc')	#one word
d.extend('abc')	#three words
d.appendleft()
d.pop()
d.popleft()

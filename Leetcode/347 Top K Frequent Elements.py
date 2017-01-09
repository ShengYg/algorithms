from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [[]for _ in nums]
        cnt = Counter(nums)
        for num, freq in cnt.items():
            bucket[len(nums) - freq].append(num)
        return list(itertools.chain(*bucket))[:k]

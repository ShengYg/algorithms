import bisect
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []
        for n in set(nums):
            bisect.insort(l, -n)
            if len(l)>3:
                l.pop()
        return -l[2] if len(l)>2 else -l[0]

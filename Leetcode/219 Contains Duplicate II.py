class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == len(set(nums)) or k == 0:
            return False
        else:
            for q in nums:
                p = [i for i, x in enumerate(nums) if x==q]
                m = [j-i for i, j in zip(p[:-1], p[1:])]
                if len(m) > 0:
                    if min(m) <= k:
                        return True
        return False

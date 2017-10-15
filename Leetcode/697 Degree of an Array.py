class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]].append(i)
            else:
                dict[nums[i]] = [i]
        ldict = {}
        for key in dict:
            ldict[key] = len(dict[key])
        length = max(ldict.values())
        ret = float('inf')
        for key in ldict:
            if ldict[key] == length:
                item = dict[key]
                ret = min(ret, max(item) - min(item) + 1)
        return ret

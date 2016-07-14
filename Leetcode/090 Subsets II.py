class Solution(object):
#method 1
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        totalset = [[]]
        for num in nums:
            totalset += [i+[num] for i in totalset if i+[num] not in totalset]
        return totalset

#method 2
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        totalset = [[]]
        i = 0
        while i < len(nums):
            count = 0
            while i+count<len(nums) and nums[i+count]==nums[i]:
                count += 1          
            for j in range(count):
                totalset += [instance + [nums[i]] for instance in totalset if instance + [nums[i]] not in totalset]
            i += count
        return totalset

#method 3
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        totalset = [[]]
        i = 0
        while i < len(nums):
            count = 0
            while i+count<len(nums) and nums[i+count]==nums[i]:
                count += 1
            for _, instance in enumerate(totalset[:]):
                for j in range(count):
                    totalset += [instance + [nums[i]]*(j+1) ]
            i += count
        return totalset

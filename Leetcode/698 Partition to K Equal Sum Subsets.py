class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 1:
            return True
        if len(nums) < k:
            return False
        if sum(nums) % k:
            return False
        subset = sum(nums)/k
        subsetsum = [0]*k
        taken = [False]*len(nums)
        subsetsum[0] = nums[len(nums) - 1]
        taken[len(nums) - 1] = True
        return self.sub(nums, subsetsum, taken, subset, k, len(nums), 0, len(nums)-1)

    def sub(self, arr, subsetsum, taken, subset, k, n, curid, limitid):
        if subsetsum[curid] == subset:
            if curid == k-2:
                return True
            return self.sub(arr, subsetsum, taken, subset, k, n, curid+1, n-1)
        for i in range(limitid, -1, -1):
            if taken[i]:
                continue
            tmp = subsetsum[curid] + arr[i]
            if tmp <= subset:
                taken[i] = True
                subsetsum[curid] += arr[i]
                next = self.sub(arr, subsetsum, taken, subset, k, n, curid, i-1)
                taken[i] = False
                subsetsum[curid] -= arr[i]
                if next:
                    return True
        return False

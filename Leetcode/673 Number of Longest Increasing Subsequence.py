class Solution(object):
    def findNumberOfLIS(self, nums):
        n = len(nums)
        cnt = [1]* n
        length = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        cnt[i] = cnt[j]
                    elif length[j]+1 == length[i]:
                        cnt[i] += cnt[j]

        maxlen = 0
        ans = 0
        for i in range(n):
            maxlen = max(maxlen, length[i]);
        for i in range(n):
            if length[i] == maxlen:
                ans += cnt[i]
        return ans

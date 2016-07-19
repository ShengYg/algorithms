class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [1]
        nums = []
        result = []
        Sum = 1
        for i in range(1, n + 1):
            Sum *= i
            fac.append(Sum)
            nums.append(i)
        k -= 1
        for i in range(1, n + 1):
            index = k / fac[n - i]
            num = nums[index]
            result.append(str(num))
            nums.remove(num)
            k %= fac[n - i]
        return ''.join(result)

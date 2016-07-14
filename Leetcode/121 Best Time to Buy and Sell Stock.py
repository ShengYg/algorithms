class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_sum = 0
        max_result = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            max_sum += diff
            if max_sum < 0:
                max_sum = 0
            max_result = max(max_result, max_sum)
        return max_result

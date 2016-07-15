class Solution(object):
	#DP
	#=======#===========#===============#===============#=============
	#		buy1		sell1			buy2			sell2
	#					buy1+price		sell1-price		buy2+price
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell1, sell2 = 0, 0
        buy1, buy2 = -float('inf'), -float('inf')
        for i in range(len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2




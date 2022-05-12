class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxi = 0
        mini = prices[0]
        for i in range(len(prices)):
            amt = prices[i] - mini
            maxi = max(amt, maxi)
            mini = min(mini, prices[i])
            
        return maxi
        
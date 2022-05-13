class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        maxi = Sum = sum(cardPoints[0:k])
        for i in range(1,k+1):
            Sum = Sum + cardPoints[-i] - cardPoints[k-i]
            maxi = max(Sum, maxi)
        return maxi
        
        
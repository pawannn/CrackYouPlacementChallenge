class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            Sum = 0
            for j in range(i,len(nums)):
                Sum = Sum + nums[j]
                if(Sum == k):
                    res += 1
        return res
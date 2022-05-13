class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum = sum + nums[j]
                if(sum%k == 0):
                    res += 1
        return res
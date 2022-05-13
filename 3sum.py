class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if(nums[i] + nums[j] + nums[k] == 0):
                        lst = []
                        lst.append(nums[i])
                        lst.append(nums[j])
                        lst.append(nums[k])
                        lst.sort()
                        if(lst not in res):
                            res.append(lst)
        return res
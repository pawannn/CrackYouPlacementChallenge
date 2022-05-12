class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = []
        nums.sort()
        for i in range(1,len(nums)):
            if(nums[i] == nums[i-1]):
               lst.append(nums[i])
        return lst
        
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x = 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[x] = nums[i]
                x += 1
        for i in range(x,len(nums)):
            nums[i] = 0
        return nums
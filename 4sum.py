class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                for c in range(b+1,len(nums)):
                    for d in range(c+1,len(nums)):
                        if(nums[a] + nums[b] + nums[c] + nums[d] == target):
                            lst = []
                            lst.append(nums[a])
                            lst.append(nums[b])
                            lst.append(nums[c])
                            lst.append(nums[d])
                            lst.sort()
                            if(lst not in res):
                                res.append(lst)
        return res
                        
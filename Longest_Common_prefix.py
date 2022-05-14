class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs)==0):
            return ""
        pre= strs[0]
        for i in range(1,len(strs)):
            while strs[i][0:len(pre)]!=pre:
                pre=pre[0:len(pre)-1]
                if len(pre)==0:
                    return ""
        return pre
        
        
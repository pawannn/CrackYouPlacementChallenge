class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        Open = ['(','[','{']
        close = [')',']','}']
        for i in range(len(s)):
            if((s[i]) in Open):
                stack.append(s[i])
            elif((s[i] in close)):
                if(Open.index(stack[-1]) == close.index(s[i])):
                    stack.pop()
                else:
                    continue
        if(stack == []):
            return True
        else:
            return False
        
        
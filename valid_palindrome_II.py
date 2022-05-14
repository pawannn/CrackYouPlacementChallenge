class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        count = 1
        stat1 = True
        while i<len(s)//2:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if s[i] == s[j-1] and count>0:
                    j -= 1
                    count -= 1
                else:
                    stat1 = False
                    break
                    
        i = 0
        j = len(s)-1
        count = 1
        stat2 = True
        while i<len(s)//2:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if s[i+1] == s[j] and count>0:
                    i += 1
                    count -= 1
                else:
                    stat2 = False
                    break
                
        return stat1 or stat2
        
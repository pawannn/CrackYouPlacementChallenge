class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lst = [] 
        top = left = 0 #k = 0 l = 0 
        down = len(matrix) # m
        right = len(matrix[0]) # n 
        while(top < right and left < down):
            for i in range(left,right):
                lst.append(matrix[top][i])
            top += 1
            
            for i in range(top,down):
                lst.append(matrix[i][right-1])
            right -= 1
            
            if(top < down):
                for i in range(right-1,left-1,-1):
                    lst.append(matrix[down-1][i])
                down -= 1 
                
            if (left < right):
                for i in range(down-1, top - 1, -1):
                    lst.append(matrix[i][left])
                left += 1
        return lst
       
                
                
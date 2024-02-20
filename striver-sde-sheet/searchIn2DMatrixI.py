## binary search
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        #locating nearest small row 

        i = 0
        j = len(matrix)-1
        near_row = 0

        while i<=j:
            mid= (i+j)//2
            element =matrix[mid][0]

            if element==target:
                return True
            elif element<target:
                near_row = mid
                i=mid+1
            else:
                j=mid-1

        start = 0
        end = len(matrix[0])-1

        while start<=end:
            mid = (start+end)//2

            if matrix[near_row][mid]==target:
                return True
            elif matrix[near_row][mid]<target:
                start=mid+1
            else:
                end=mid-1
        return False 
     
#modulo calculation [My original approach]
    
class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        
        start = 0
        end = (len(matrix[0])*len(matrix))-1
        endLimit = (len(matrix[0])*len(matrix))-1
        startLimit = 0
        
        def locate(n):
            if n>endLimit:
                return False
            if n<startLimit:
                return False
            
            r = n//len(matrix[0])
            c = n%len(matrix[0])
            
            return matrix[r][c]
        
        while start<=end:
            mid = (start+end)//2
            
            
            if locate(mid)==target:
                return True
            elif locate(mid)<target:
                start = mid+1
            else:
                end = mid-1
                
        return False        
            
            
            





 
        
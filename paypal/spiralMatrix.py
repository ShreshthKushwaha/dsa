##Recursion se

class Solution:
    def spiralOrder(self, matrix):
        def spiral(i,j,d):
            if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]==-101:
                return []
            temp = matrix[i][j] 
            matrix[i][j] = -101
            if d==1:
                next_arr = spiral(i,j+1,d)                
                if next_arr==[]:
                    return [temp]+spiral(i+1,j,2)
                else:                    
                    return [temp]+next_arr
            elif d==2:               
                next_arr = spiral(i+1,j,d)               
                if next_arr==[]:
                    return [temp]+spiral(i,j-1,3)
                else:    
                    return [temp]+next_arr
            elif d==3:
                next_arr = spiral(i,j-1,d) 
                if next_arr==[]:
                    return [temp]+spiral(i-1,j,4)
                else:
                    return [temp]+next_arr

            elif d==4:
                next_arr = spiral(i-1,j,d) 
                if next_arr==[]:
                    return [temp]+spiral(i,j+1,1)
                else:
                    return [temp]+next_arr

        return spiral(0,0,1)     

###iterative 
class Solution:
    def spiralOrder(self, matrix):
        ans = []

        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        
        while (top<=bottom and left<=right):
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1

            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1  
            ##wapasi mai check karo ki mamla khatam to nai hogya h vertical side se
            if top<=bottom:
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])
                bottom-=1
            ##wapasi mai check karo ki mamla khatam to nai hogya h horizontal side se    
            if left<=right:    
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        return ans     





            


        
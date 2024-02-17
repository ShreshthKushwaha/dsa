##O(m+n) space solution
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_mem = set()
        col_mem = set()


        

        
            


        map = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row_mem.add(i)
                    col_mem.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row_mem or j in col_mem:
                    matrix[i][j]=0
###----O(1) space solution store logs in array itself and use a var for mat[0][0]
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_o = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if j!=0:
                        matrix[i][0]=0 
                        matrix[0][j]=0
                    else:
                        col_o=0
                        matrix[i][0]=0

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        print (matrix)            

        if matrix[0][0]==0:
            for j in range(1,len(matrix[0])):
                matrix[0][j]=0


        if col_o==0:
            for i in range(0,len(matrix)):
                matrix[i][0]=0
                                           

                             
                



                    










                                             
                                






        
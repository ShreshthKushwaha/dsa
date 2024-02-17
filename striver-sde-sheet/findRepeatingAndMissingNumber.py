class Solution:
    def findTwoElement( self,arr, n): 
        #x missing,y doubling
 
        #x-y
        xDiffy=(n*(n+1)/2)-sum(arr)
    
        sqrSum = 0
        for e in arr:
            sqrSum+=(e**2)
        xsqrDiffysqr = ((n*(n+1)*((2*n)+1))//6)-sqrSum
        xSumy=xsqrDiffysqr//(xDiffy)
    
        #x-y+x+y=2x
        
    
        missing = int((xDiffy+xSumy)/2)
        doubling =int(xSumy-missing)

        return (doubling,missing)
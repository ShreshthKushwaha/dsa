class Solution:
    def myPow(self, x: float, n: int) -> float:

        def search(p,res):
            print (p,res)
            if p==abs(n):
                return res
            if p>abs(n):
                return search(p-1,res/x)    
            return search(p*2,res*res)




        if n>=0:    
            if n==0:
                return 1

            return search(1,x)
        else:
            
            return 1/search(1,x)            

        
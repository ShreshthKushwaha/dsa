##binary increment but O(1) space

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

        
##space but faster

class Solution:
    def myPow(self, x: float, n: int) -> float:
        mem = {}
        
        
        def solve(x,n):
            if n==2:
                return x*x
            if n==1:
                return x
            if n==0:
                return 1
            if n in mem:
                return mem[n]
            ans = 1
            if n%2==0:
                ans = solve(x,n//2)*solve(x,n//2)
            else:
                ans = solve(x,n//2)*solve(x,(n//2)+1)
            mem[n]=ans    
            return ans    
        
        if n>=0:
            return solve(x,n)
        else:
            return 1/solve(x,-n)
            
    
                
                
                
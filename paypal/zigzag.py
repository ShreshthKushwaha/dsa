#-----brute -------

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        hm = {}
        r = 0
        d =-1
        for i in range(len(s)):
            if r not in hm:
                hm[r]=[s[i]]
            else:
                hm[r].append(s[i])
        
            if r==0 or r==numRows-1:
               
                if d==1:
                    d = -1
                else:
                    d = 1
            if d==1:
                r+=1
            else:
                r-=1
        print (hm)
        ans = ""
        for k in hm:
            ans+="".join(hm[k])
        return ans                         

#------optimal-------
    
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows==1:
            return s
        
        ans = ""
        
        for r in range(numRows):
            downStep = 2*(numRows-1-r)
            upStep = 2*r
            idx = r
            down =True

            while idx<len(s):

                ans+=s[idx]
                if r==0:
                    idx+=downStep
                elif r==numRows-1:
                    idx+=upStep    
                else:    
                    if down == True:
                        idx+=downStep
                    else:
                        idx+=upStep
                    if down==True:
                        down = False
                    else:
                        down=True        
                 
            print (ans)    
          
        return ans    







                                 




            
            


            
        
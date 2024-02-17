class Solution:
    def findPairs(self, nums, k: int) -> int:

        hm = {}
        for e in nums:
            if e in hm:
                hm[e]+=1
            else:
                hm[e]=1   

        count = 0
        for key in hm:
            if k==0:
                if hm[key]>1:
                    count+=1
            else:
#    ---    ----- 
#    -----  ---     in both cases if we add 2(->k(->diff)) to one we ll get other                               
                if key+k in hm:
                    count+=1                

        
        return count
        
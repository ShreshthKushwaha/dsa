class Solution:
    def canArrange(self, arr, k) -> bool:
        hm = {}
        for i in range(len(arr)):
            arr[i]=arr[i]%k
        print (arr)    
        for e in arr:
            if e not in hm:
                hm[e]=1
            else:
                hm[e]+=1  
        print (hm)           
        for key in hm:
            if key==0:
                if hm[key]%2!=0:
                    return False
            elif k-key not in hm or hm[key]!=hm[k-key]:
                return False
        return True            
        
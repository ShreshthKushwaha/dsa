class Solution:
    def combinationSum2(self, candidates, target: int):

        candidates.sort()
        res=[]

        def find(i,op,s):
            if i>=len(candidates):
                if s==target:
                        res.append(op)
                return
            if s>target:
                return    

            similar = 0
            for idx in range(i,len(candidates)):
                if candidates[idx]==candidates[i]:
                    similar+=1
         
                   
            for count in range(1,similar+1):
               
                find(i+similar,op+[candidates[i]]*count,s+(candidates[i]*count))
            find(i+similar,op,s)  
        find(0,[],0)      

        return res        


        
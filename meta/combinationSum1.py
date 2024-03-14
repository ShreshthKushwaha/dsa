class Solution:
    def combinationSum(self, candidates, target):

        res = []


        def make(i,arr,sum):
            
            if i>=len(candidates):
                if sum==target:
                    res.append(arr[0:])
                return
            if sum>target:
                return    
            print (i,arr,sum)
            ##agar hum make(i+1,arr+[candidates[i]],sum+candidates[i]) kara toh repeat honge kuki candidate[i] do cases mai add hora h
            make(i+1,arr,sum)
            ##isse theek hum yeh kar den isse add hojayega phir aage bhi bd payega or retain bhi kr payega
            make(i,arr+[candidates[i]],sum+candidates[i])  
           
        make(0,[],0)
        return res                

                



        
class Solution:
    def sortedSquares(self, nums):


        pivot = None
        for i in range(len(nums)):
            if i<len(nums)-1:
                if nums[i]**2>nums[i+1]**2:
                    pivot = i
        if pivot!=None:
            i = pivot
            j = pivot+1
        else:
            j = 0
            i=-1          
        res = []
        while i>=0 and j<len(nums):
            if abs(nums[i])==abs(nums[j]):
                res.append(nums[i]**2)
                i-=1             
            elif abs(nums[i])>abs(nums[j]):
                res.append(nums[j]**2)
                j+=1

            elif abs(nums[i])<abs(nums[j]):  
                res.append(nums[i]**2)
                i-=1    
        while i>=0:
            res.append(nums[i]**2)
            i-=1
        while j<len(nums):
            res.append(nums[j]**2)
            j+=1
        return res                  



        
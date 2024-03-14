class Solution:
    def subarraySum(self, nums, k: int) -> int:

        for i in range(len(nums)):
            if i!=0:
                nums[i]=nums[i]+nums[i-1]

        count = 0
        hm = {}

        for e in nums:
            if e-k in hm:
                count+=hm[e-k]
                print (e-k)
            if e==k:
                count+=1    

            if e not in hm:
                hm[e]=1
            else:        
                hm[e]+=1   
        return count      





        
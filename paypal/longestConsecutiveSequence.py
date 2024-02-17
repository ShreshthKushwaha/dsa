#better approach

class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        finalAns = 1

        ans = None
        for i in range(len(nums)):
            if ans==None:
                ans=1
                lastNum = nums[i]
            else:
                if nums[i]==lastNum+1:
                    ans+=1
                else:
                    if nums[i]!=lastNum:
                        ans = 1
                finalAns = max(finalAns,ans)
                lastNum = nums[i]
        return finalAns          
##optimal approach

class Solution:
    def longestConsecutive(self, nums):
        hm = {}
        for e in nums:
            if e not in hm:
                hm[e]=1
        mem = {}           

        

        def getSequence(n):
            if n in mem:
                return mem[n]
            if n not in hm:
                return 0
            mem[n]=1+getSequence(n-1) 
            return mem[n]
        ans = 0  

        for e in nums:
            ans = max(ans,getSequence(e))
        return ans    









                  





        
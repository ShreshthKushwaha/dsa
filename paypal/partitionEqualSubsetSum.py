##Recursion and Memoization-->MLE
class Solution:
    def canPartition(self, nums) -> bool:

        if sum(nums)%2==1:
            return False

        overall = sum(nums)

        mem ={}

        def pick(i,currSum):
            if i>=len(nums):
                return False
            if overall - currSum == currSum:
             
                return True
            if (i,currSum) in mem:
                return mem[(i,currSum)]  

            a = pick(i+1,currSum+nums[i])
            b = pick(i+1,currSum)

            mem[(i,currSum)] = a or b

            return mem[(i,currSum)]
        return pick(0,0)     
##better
class Solution:
    def canPartition(self, nums) -> bool:

        if sum(nums)%2==1:
            return False

        overall = sum(nums)

        mem ={}

        def pick(i,currSum):
            if i>=len(nums):
                if currSum == 0:
                    return True
                return False
            if currSum<0:
                return False    
            
            if (i,currSum) in mem:
                return mem[(i,currSum)]  

            a = pick(i+1,currSum-nums[i])
            b = pick(i+1,currSum)

            mem[(i,currSum)] = a or b

            return mem[(i,currSum)]
        return pick(0,overall//2)                
                           
        
##---extra space..


#----mera solution-----

class Solution:
    def moveZeroes(self, nums) -> None:

        i = 0
      
        j = 0


        while j<len(nums):
            ##pehle i ko zero wale par lao
            while i<len(nums) and nums[i]!=0:
                i+=1
            #agar i j se aage nikal gya hai toh j ko i ke aage lao
            j = max(j,i+1)
            #j ko non zero par lao
            while j<len(nums) and nums[j]==0:
                j+=1
            #replace/swap karo or dono ko aage karo    
            if j<len(nums) and i<len(nums):
                nums[i],nums[j]= nums[j],nums[i]
                i+=1
                j+=1
        print (nums)  
#------clean solution        
        
class Solution:
    def moveZeroes(self, nums) -> None:

        left = 0
      
        right = 0

        while right<len(nums):
            if nums[right]==0:
                right+=1
            else:
                nums[right],nums[left]=nums[left],nums[right]
                left+=1
                right+=1        
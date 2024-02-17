class Solution:
    def search(self, nums, target) -> int:

        ##searching the smallest point

        i = 0
        j = len(nums)-1
        smallest = 0

        while i<=j:
            mid = (i+j)//2
            print (i,j)
            if nums[mid]<nums[(mid+1)%len(nums)] and nums[mid]<nums[(mid-1+len(nums))%len(nums)]:
                smallest = mid
          
            if nums[mid]>nums[j]:
                i=mid+1   
            else:
                j=mid-1    
            

                    
            
        ##once I have smallest...lets run binary search 
        print (smallest)

        def binSearch(i,j,t):
            start = i
            end = j
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==t:
                    return mid
                elif nums[mid]<t:
                    start=mid+1
                else:
                    end=mid-1
            return -2**31
        return max(-1,binSearch(smallest,len(nums)-1,target),binSearch(0,smallest,target))                            
              




        
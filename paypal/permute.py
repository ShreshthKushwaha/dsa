class Solution:
    def permute(self, nums):
        ans = []
        def permute(arr,result):
            if len(arr)==0:
                ans.append(result)
                return
            for i in range(len(arr)):           
                permute(arr[0:i]+arr[i+1:],result+[arr[i]])
        permute(nums,[])        
        return ans   
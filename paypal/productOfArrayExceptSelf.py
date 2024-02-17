class Solution:
    def productExceptSelf(self, nums):


        left = []
        right = []
        ans = []

        product = 1

        for i in range(len(nums)):
            ans.append(product)
            product = product*nums[i]
        product = 1

        for i in range(len(nums)-1,-1,-1):
            ans[i]=ans[i]*product
            product = product*nums[i]

        return ans      

        
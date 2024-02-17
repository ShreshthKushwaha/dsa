class Solution:
    def twoSum(self, nums, target):

        hm = {}


        for i in range(len(nums)):
            if (target-nums[i]) in hm:
                return [hm[target-nums[i]],i]
            hm[nums[i]]=i
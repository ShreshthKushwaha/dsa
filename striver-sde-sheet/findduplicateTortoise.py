class Solution:
    def findDuplicate(self, nums) -> int:

        slow = nums[0]
        fast = nums[0]
        flag = False


        while slow!=fast or flag==False:
            slow = nums[slow]
            fast=nums[nums[fast]]
            flag = True

        print (slow,fast) 
        slow = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast=nums[fast]


        return fast





        
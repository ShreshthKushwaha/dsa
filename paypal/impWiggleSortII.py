class Solution:
    def wiggleSort(self, nums) -> None:

        ###hypotheses-->
        ####[a b c d e f g h] ---><--- can have problems as difference will reduce ..so <---<---is better
        curr = nums[0:]
        curr.sort()
        idx = len(nums)-1
        ##filling odd 

        for i in range(1,len(nums),2):
            nums[i]=curr[idx]
            idx-=1
        for i in range(0,len(nums),2):
            nums[i]=curr[idx]
            idx-=1
                
                              
        """
        Do not return anything, modify nums in-place instead.
        """
        
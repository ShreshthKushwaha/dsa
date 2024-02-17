class Solution:
    def trap(self, height) -> int:


        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        res = 0

        while left<right:
            if height[left]<=height[right]:
                if height[left]<left_max:
                    res+=(left_max-height[left])
                left_max = max(left_max,height[left])    
                left+=1
            else:
                if height[right]<right_max:
                    res+=(right_max-height[right])
                right_max = max(right_max,height[right])
                right-=1
        return res            





        
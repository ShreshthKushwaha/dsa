# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        
        ans = [-2**31]


        def travel(root):
            if root==None:
                return 0
            left = travel(root.left)  
            right =  travel(root.right)   


            ans[0] = max(left+right+root.val,ans[0])


            return max(left+root.val,right+root.val,root.val,0)
        travel(root)

        return ans[0]    
        
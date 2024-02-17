# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):

        ans = []


        def inorder(root,h):
            if root==None:
                return 
            ##making sure our array has place for current height
            if len(ans)<=h:
                ans.append(root.val)
            else:
                ans[h]=root.val

            
            inorder(root.left,h+1)
            
            
            inorder(root.right,h+1)
        inorder(root,0)
        return ans                
        
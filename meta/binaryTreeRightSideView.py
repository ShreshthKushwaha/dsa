# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):

        ans = []


        def preorder(root,h):
            
            if root==None:
                return
            #agar us index par koi nahin hai toh khud ko dalo or bar wale traversals m wo replace hojayega agar koi orr right  mai ayega    
            if len(ans)<=h:
                ans.append(root.val)
            else:
                ans[h]=root.val    
            preorder(root.left,h+1)    
            
            preorder(root.right,h+1)
        preorder(root,0)    

        return ans        
                   
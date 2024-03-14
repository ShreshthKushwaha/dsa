# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:


        def getAll(root):
            if root==None:
                return []
            res = []    
            left = getAll(root.right)
            right = getAll(root.left)
            if left==[] and right==[]:
                res = [str(root.val)]
            else:    

                for e in left:
                    res.append(str(root.val)+str(e))
                for e in right:
                    res.append(str(root.val)+str(e)) 
            return res
        arr =  (getAll(root))  
        ans = 0
        for e in arr:
            ans+=int(e)
        return ans         



                
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dia = 0
    def diameterOfBinaryTree(self, root) -> int:




        def calculate(root):
            if root==None:
                return 0
            right = 1+calculate(root.right)
            left = 1+calculate(root.left)
            self.dia = max(right+left-2,self.dia)


            return max(right,left) 
        calculate(root)
        return self.dia    
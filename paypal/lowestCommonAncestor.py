# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):


        def find(root):
            if root==None:
                return None
            if root==p or root==q:
                return root
            left = find(root.left)
            right = find(root.right)

            if left and right:
                return root
            if left:
                return left
            if right:
                return right
            return None
        return find(root)   
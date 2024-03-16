# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root):
        hm = defaultdict(list)
        def traverse(root,x,y):
            if root==None:
                return
            hm[(x,y)].append(root.val)    
            hm[(x,y)].sort()
            traverse(root.left,x-1,y+1)
            traverse(root.right,x+1,y+1)
        traverse(root,0,0)    

        res = []
        print (hm)
        for x,y in sorted(hm):
            if x not in hm:
                hm[x]=hm[(x,y)]
            else:
                hm[x]+=hm[(x,y)]   

        
            del hm[(x,y)]
        res = []
        for k in sorted(hm):
            res.append(hm[k])
        return res    

            


        
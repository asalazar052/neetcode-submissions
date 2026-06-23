# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        res = False
        
        def dfs(node):

            nonlocal res
            
            if not node:
                return
            
            if isSub(node, subRoot):
                res = True
            
            dfs(node.left)
            dfs(node.right)

                
                
        def isSub(r1, r2):
            
            if not r1 and not r2:
                return True
            
            if (not r1 and r2) or (r1 and not r2) or (r1.val != r2.val):
                return False
            
            return isSub(r1.left, r2.left) and isSub(r1.right, r2.right)
            
        dfs(root)

        return res
            

            



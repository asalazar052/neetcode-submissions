# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.res = True

        def helper(pNode, qNode):
            if not pNode and not qNode:
                return
            
            
            
            if (not pNode or not qNode) or (pNode.val != qNode.val):
                self.res = False
                return
            
            helper(pNode.left, qNode.left)
            helper(pNode.right, qNode.right)
            
            return
        
        helper(p, q)

        return self.res



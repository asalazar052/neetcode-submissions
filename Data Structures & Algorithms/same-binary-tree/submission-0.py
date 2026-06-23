# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        
        def helper(pNode, qNode):
            if not pNode and not qNode:
                return
            
            if (pNode and not qNode) or (not pNode and qNode) or pNode.val != qNode.val:
                self.same = False
                return
            
            helper(pNode.left, qNode.left)
            helper(pNode.right, qNode.right)

        
        helper(p, q)
        return self.same
            



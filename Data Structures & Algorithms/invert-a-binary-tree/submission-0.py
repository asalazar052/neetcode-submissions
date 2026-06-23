# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def helper(node):
            if not node:
                return
            
            if node.left and node.right:
                node.left, node.right = node.right, node.left
            elif node.left and not node.right:
                node.left, node.right = None, node.left
            elif not node.left and node.right:
                node.left, node.right = node.right, None
            
            helper(node.left)
            helper(node.right)
            
        helper(root)

        return root

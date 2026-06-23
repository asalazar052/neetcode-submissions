# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        #returns the current height at that node
        def helper(node):
            
            if not node:
                return 0

            leftHeight = helper(node.left)
            rightHeight = helper(node.right)

            self.res = max(self.res, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)
    
        helper(root)
        return self.res
            
        
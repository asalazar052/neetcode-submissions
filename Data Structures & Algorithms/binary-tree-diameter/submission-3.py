# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0
        
        def helper(node): # returns the height at each node
            if not node:
                return 0
            
            left = helper(node.left) # Calculates height of left subtree
            right = helper(node.right) # Calculates height of right subtree

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)
        
        helper(root)
        return self.diameter


            

        
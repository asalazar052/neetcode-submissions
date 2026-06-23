# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = True

        def dfs(node, curMin, curMax):

            nonlocal res

            if not node:
                return
            
            if node.val >= curMax or node.val <= curMin:
                res = False
            
            # Left subtree: curMax gets updated to the current val, curMin stays the same
            dfs(node.left, curMin, node.val)
            # Right subtree: curMin gets updated to the current val, curMin stays the same
            dfs(node.right, node.val, curMax)
            
        
        dfs(root, float('-inf'), float('inf'))
        return res

'''
In the left subtree, no values can be greater than the current node
In the right subtree, no values can be less than the current node

                5
            4       6
        none none  3 7

In this example, 3's min is 5 and max is 6, but 4's min is -inf and max is 5
'''



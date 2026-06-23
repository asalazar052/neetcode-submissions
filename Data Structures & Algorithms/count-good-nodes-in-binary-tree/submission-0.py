# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        goodNodes = 0

        def dfs(node, curMax):

            nonlocal goodNodes

            if not node:
                return
            
            if node.val >= curMax:
                goodNodes += 1
            curMax = max(node.val, curMax)

            dfs(node.left, curMax)
            dfs(node.right, curMax)
        
        dfs(root, root.val)

        return goodNodes

'''
- On any path, take the value of the max of that path. 
- If the upcoming node is greater than or equal to, it is considered a good node

'''
        
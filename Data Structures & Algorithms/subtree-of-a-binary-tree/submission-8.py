# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #if not subRoot: return True

        self.isSubtree = False

        def helper(startNode, startSub): # checks if subtree is the same starting from that node
            if not startNode and not startSub:
                return True

            if startNode and startSub and startNode.val == startSub.val:
                return helper(startNode.left, startSub.left) and helper(startNode.right, startSub.right)
            
            return False

            

        
        def dfs(node, subNode):
            if not subNode: # edge case
                return True
            if not node: # edge case
                return False
            
            if helper(node, subNode):
                return True

            return dfs(node.left, subNode) or dfs(node.right, subNode)

            

        return dfs(root, subRoot)
         
            

        




            
              

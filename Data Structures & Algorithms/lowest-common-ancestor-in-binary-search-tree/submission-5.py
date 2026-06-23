# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        cur = root

        while cur:
            
            # p must be ancestor of itself
            if cur.val == p.val:
                return cur
            
            # p must be ancestor of itself
            elif cur.val == q.val:
                return cur
            
            # disregard entire right subtree if both p and q are on the left part
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            # disregard entire left subtree if both p and q are on the right part
            elif q.val > cur.val and p.val > cur.val:
                cur = cur.right
            
            # This case only occurs if the current node has p.val and q.val on opposite sides
            else:
                return cur

        
'''

if (p.val <= cur.val and q.val > cur.val) or (q.val <= cur.val and p.val > cur.val)

   2
  1 None

'''
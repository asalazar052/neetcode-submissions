# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        queue = deque([root])

        while queue:
            cur = queue.popleft()
            if (p.val <= cur.val and q.val >= cur.val) or (q.val <= cur.val and p.val >= cur.val):
                return cur

            queue.append(cur.left)
            queue.append(cur.right)
            
        return None

        
'''

if (p.val <= cur.val and q.val > cur.val) or (q.val <= cur.val and p.val > cur.val)

   2
  1 None

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(preO, inO):
            if not preO or not inO:
                return
            
            root = TreeNode(preO[0], None, None)
            
            # Index of root in pre-order array, which allows us to partition subtrees
            index = inO.index(preO[0])

            # Left subtree
            root.left = dfs(preO[1:index + 1], inO[0:index])

            # Right Subtree
            root.right = dfs(preO[index + 1:], inO[index + 1:])

            return root
        
        return dfs(preorder, inorder)

            

            


'''
What does preorder tell us? 
preorder[0] is our root

What does inorder tell us?
where inorder[i] = preorder[0], anything to the left is our left subtree, anything to the right
is our right subtree

'''
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
            
            root = TreeNode(preO[0])
            m = inO.index(preO[0])
            root.left = dfs(preO[1:m + 1], inO[:m])
            root.right = dfs(preO[m + 1:], inO[m + 1:])

            return root

        return dfs(preorder, inorder)
            








'''
dfs in order:

    if not none:
        return
    
    dfs(node.left)
    print(node.val)
    dfs(node.right)

Move all the way left, take care of leftmost node all the way back up, then take care of right subtree

[2,1,3,4]

dfs pre order:

    if not none:
        return
    
    print(node.val)
    dfs(node.left)
    dfs(node.right)

[1,2,3,4]

Take care of the current node then move left. Once we finish, we do the same to right subtree

'''
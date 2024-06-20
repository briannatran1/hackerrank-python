# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''req:
            - fn takes in root of binary tree, 2 nodes
        '''
        # base case: root is None, or root is equal to p or q -> found one of the nodes
        # recursively call fn on left and right subtrees passing in p and q
        # if left and right or not null, current root is LCA so return root
        # else, return the one that isn't null
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right

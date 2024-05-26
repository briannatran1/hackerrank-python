# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''req:
            - fn takes in root of binary tree
            - invert tree and return its root
        '''
        # base case: root is null
        # initialize right and left vars and recursively call fn on right and left children
        # reassign left to right and right to left
        # return root
        if not root:
            return root
        
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left

        return root

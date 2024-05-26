# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''req:
            - fn takes in a root and an int
            - return subtree w/ node in BST that equals given val

            >>> [4,2,7,1,3], val = 2
            [2, 1, 3]
        '''
        # while root does not equal null and val of root is not target,
        # if val of root > target, search left subtree
        # else, search right subtree
        # return root
        while root and root.val != val:
            if root.val > val:
                root = root.left
            else:
                root = root.right
        
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''req:
            - fn takes in root and a key (int)
            - delete node w/ key in BST
            - return root node reference

            1. search for node to remove
            2. delete node if found
        '''
        # base case: root is null 
        # if key < root.val, recursively call fn on left child
        # elif key > root.val, recursively call fn on right child
        # else, root has one child or no child
        # if root has only one child, replace root w/ that child
        # else, root has 2 children
        if not root: # base case
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # do deletion since node is found
        else: # only has 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # find min (keep going left) from right subtree
            else:
                node = root.right

                while node.left:
                    node = node.left # finds deepest left child in right subtree
                
                root.val = node.val # sets val to deepest left child val
                # recursively deletes node
                root.right = self.deleteNode(root.right, node.val)
        
        return root

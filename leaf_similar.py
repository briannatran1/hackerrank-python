# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''req:
            - fn takes in 2 binary trees
            - return true if they are leaf-similar
            - leaf similar: last node sequence is the same

            >>> root1 = [1,2,3], root2 = [1,3,2]
            false

            >>> root1 = [3,5,1,6,2,9,8,null,null,7,4], 
            root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
            true
        '''
        # DFS recursion traversal of each tree -> helper fn
        # base case: root is null
        # if root has no right or left children, it is a leaf node and we append the value to leaf
        # call dfs recursively for right and left children of root
        # initialize 2 lists to store leaf values
        # call dfs on root1 and root2 to populate respective lists
        # compare leaf sequences in lists
        def dfs(root, leaf):
            '''performs dfs traversal of tree
            
                leaf -> list that stores values 
                root -> current node being processed
            '''
            if not root: 
                return
            
            if not root.left and not root.right:
                leaf.append(root.val)
                return 

            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2

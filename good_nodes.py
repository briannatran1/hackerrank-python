# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''req:
            - inputs: root of a binary tree
            - output: num 
            - good = path from root to X no nodes w/ a value > X
        '''
        # base case: root is null -> return 0
        # if root.val >= max, set max to root.val and increment self.good_nodes
        # recursively call fn for root.left and root.right w/ max
        # call dfs fn on root
        # return self.good_nodes
        self.good_nodes = 0
        def dfs(root, maximum = float('-inf')):
            if not root:
                return 
            
            if root.val >= maximum:
                maximum = root.val
                self.good_nodes += 1
            
            dfs(root.left, maximum)
            dfs(root.right, maximum)
        
        dfs(root)
        return self.good_nodes

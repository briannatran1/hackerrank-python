# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''req:
            - inputs: root of binary tree, integer
            - output: integer - number of paths where sum equals target
            - path must go downwards

            - DFS
        '''
        def dfs(root, start, sum):
            '''Performs DFS on the tree
                - inputs: root(curr node), start (bool to indicate it new path is 
                starting), sum (curr sum needed to reach target)

            '''
            if not root: # base case
                return 
            
            sum -= root.val # subtracting node value from curr sum
            if sum == 0: # reached target
                self.count += 1

            dfs(root.left, False, sum)
            dfs(root.right, False, sum)
            if start:
                # continues current path, not new path
                dfs(root.left, True, targetSum)
                dfs(root.right, True, targetSum)
        
        dfs(root, True, targetSum)
        return self.count

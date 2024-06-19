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


# stack solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''req:
            - fn given 
        '''
        # init stack to tuple root node and root.val
        # init count var to 0
        # loop while stack has elems in it,
        # pop tuple and assign to node and max_num
        # if node.val >= max_num, increment count
        # set max_num to the max of the 2
        # if node.left is not null, append node.left and max_num to stack
        # do the same with node.right
        # return count
        stack = [(root, root.val)]
        count = 0

        while stack:
            node, max_num = stack.pop() #
            if node.val >= max_num:
                count += 1
            max_num = max(max_num, node.val)

            if node.left:
                stack.append((node.left, max_num))
            if node.right:
                stack.append((node.right, max_num))
        
        return count

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''req:
            - fn takes in the root of a binary tree
            - return its max depth: num of nodes along longest path starting at root node

            >>> root = [3,9,20,null,null,15,7]
            3
        '''
        # base case: empty tree -- end of path is reached
        # count left child depth using recursion
        # count right child depth using recursion
        # return the largest depth + 1 (root)
        if root == None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''req:
            - fn takes in the root of a binary tree
            - return its max depth: num of nodes along longest path starting at root node

            >>> root = [3,9,20,null,null,15,7]
            3

            iterative approach
        '''
        # base case: root is null
        # initialize a stack containing root node and its depth
        # initialize a res var --> keeps track of max depth
        # loop until stack is empty
        # pop node and its depth from stack
        # if node is not null,
        # update res to max value of either curr res or curr depth
        # append left child and right child of curr node to stack along w/ its depth
        # return res
        if not root: 
            return 0

        stack = [[root, 1]]
        res = 1
        
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return res

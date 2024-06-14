# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''req:
            - fn takes in root of binary tree
            - return smallest level (int)
            - level of root is 1 and so on

            - BFS: search level by level
            - edge cases: no root -> return 0
        '''
        # declare max_sum, level, and max_level
        # init deque with root in it
        # iterate while there are still elements in the queue
        # increment level 
        # init curr_sum to 0
        # iterate over all nodes at curr level
        # pop off element in front of queue
        # add node val to curr_sum
        # enqueue children in that popped off element
        # after processing all nodes at current level, update max_sum
        # and max_level if needed
        # return max_level
        max_sum = float('-inf')
        level = 0
        max_level = 0
        q = deque([root])

        while q:
            level += 1 
            curr_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if max_sum < curr_sum:
                max_sum = curr_sum
                max_level = level
        
        return max_level

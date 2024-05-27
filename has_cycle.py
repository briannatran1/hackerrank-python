# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''req:
            - fn takes in head of LL
            - return True if LL has a cycle
            - else, return False
        '''
        # initialize fast and slow pointers to head of LL
        # enter a loop while fast and fast.next are not null
        # move fast 2 steps ahead and slow 1 step ahead
        # if fast is equal to slow, return True
        # return False if loop is exited 
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        
        return False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''req:
            - inputs: head of LL
            - output: null or node where cycle begins
            - 

            cycle -> slow/fast pointers
        '''
        # init slow and fast pointers to head
        # loop while fast and fast.next are not null
        # move slow 1 step ahead
        # move fast 2 steps ahead
        # if slow == fast --> cycle, so set slow back to start of cycle
        # move both pointers at same pace until they meet again
        # met node = starting point of cycle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None

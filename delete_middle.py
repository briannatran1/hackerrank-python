# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''req:
            - fn takes in head of LL
            - delete middle node and return LL
            - middle node: size of LL // 2

            >>> [1,2,3,4]
            1 -> 2 -> 4

            >>> head = [1,3,4,7,1,2,6]
            1 -> 3 -> 4 -> 1 -> 2 -> 6
        '''
        # base case: head is null --> nothing to delete
        # create dummy node prev
        # set prev.next to head 
        # initialize fast and slow pointers
        # traverse LL using 2 pointer technique
        # by the time fast reaches the end of the list, 
        # slow will be at the node just before the middle node
        if not head:
            return None
        
        prev = ListNode(0)
        prev.next = head
        slow = prev
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # skips over middle node and points to node after middle node
        slow.next = slow.next.next 
        # return list; prev is dummy and prev.next is start of LL
        return prev.next

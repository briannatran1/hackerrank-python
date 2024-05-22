# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''req:
            - fn takes in the head of an LL
            - return reordered list
            - 1st node = odd, etc.
            - relative order of both odd and even should be the same as in input
            - space: O(1)
            - time: O(n)

            reordered: group all odd indices nodes together then even ones after

            >>> head = [1,2,3,4,5]
            1 -> 3 -> 5 -> 2 -> 4
        '''
        # edge case: if list is empty or has only 1 node --> return head
        # initialize odd var and set to head, and even to head.next
        # initialize even_head to keep track of even list
        # iterate through LL while there are even nodes left to process
        # update odd.next to the node after next --> skips even node
        # do the same with even --> skips odd
        # after looping, link last node in odd to head of even list
        # return head
        if head == None or head.next == None:
            return head

        odd = head
        even = head.next
        even_head = even
        
        while even != None and even.next != None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head

        return head

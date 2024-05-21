# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''req:
            - fn takes in 2 heads of sorted LL
            - merge 2 lists into one sorted one and return the head

            >>> list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4
            1 -> 1 -> 2 -> 3 -> 4 -> 4
        '''
        # intialize curr and dummy to a new node
        # iterate through LL while there l1 and l2 are not null
        # if val in l1 is less than l2, set curr.next to list1
        # then update list1 to next val of list1
        # else, we will do the same thing w/ list 2
        # after, we need to update curr to use the next val
        # after we reach the end of a one list, set curr.next to the other 
        # return head.next 
        head = ListNode() # placeholder
        curr = head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2 # links the rest of remaining list w/ leftover nodes
        return head.next # starting node since head was a placeholder

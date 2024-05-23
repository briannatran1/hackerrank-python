# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''req:
            - fn takes in head of a sorted LL
            - delete all duplicates and return LL

            >>> head = [1,1,2]
            1 -> 2
        '''
        # initalize curr var to head
        # iterate through LL while curr is not null and there's next val after curr
        # if val at curr and next are the same, 
        # assign curr.next to the next next val
        # else move curr one forward
        # return head
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head

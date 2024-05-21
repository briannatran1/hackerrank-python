# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''req:
            - fn takes in a head node of LL
            - return reversed LL

            >>> head = [1,2,3,4,5]
            [5,4,3,2,1]
        '''
        # initialize 2 pointers: prev, curr
        # iterate through LL while curr isn't None
        # initialize temp var to save list
        # update temp to store next of curr
        # update next pointer of curr to point to prev
        # move prev to curr and curr to temp
        # continue until curr is null
        # return prev --> head of reversed LL
        prev = None
        curr = head 

        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        
        return prev

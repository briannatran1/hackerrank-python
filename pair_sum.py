# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''req:
            - fn takes in head of even LL
            - twin: n-1-i node
            - twin sum: sum of node and its twin
            - return max twin sum of LL
        '''
        # initialize slow, fast pointers --> reaches to middle in one go
        # initialize max_twin_sum var
        # find middle of LL by looping through LL while fast and fast.next are not null
        # reverse second part of LL
        # get max sum of pairs
        slow = head
        fast = head
        max_twin_sum = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # curr is set to slow (middle of LL) 
        # prev will keep track of reversed part of list
        curr, prev = slow, None

        # set curr.next to prev --> reverses list
        # move prev to curr node
        # move curr to next node in og list
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # prev points to head of reversed list
        while prev:
            max_twin_sum = max(max_twin_sum, head.val + prev.val)
            prev = prev.next
            head = head.next
        
        return max_twin_sum

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1, l2):
        '''merges 2 sorted lists into 1 sorted list'''
        # makes the merged list
        dummy = ListNode(0)
        tail = dummy

        # sorting
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            # moves onto next node
            tail = tail.next
        
        # pushes rest of lists to merged list if not empty
        if l1 != None:
            tail.next = l1
        elif l2 != None:
            tail.next = l2
        
        # returns head of merged list
        return dummy.next
            

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''recursively sorts list'''
        # base case
        if not head or not head.next:
            return head
        
        # slow/fast technique -- finds middle node
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next # moves 1 step
            fast = fast.next.next #moves 2 steps

        mid = slow.next
        slow.next = None # breaks list into 2 halves

        # sorts
        left = self.sortList(head) 
        right = self.sortList(mid)

        # merge sorted halves
        return self.merge(left,right)

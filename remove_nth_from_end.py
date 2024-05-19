# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''req: 
            - edge case: if n > 1 when tail == None and head not null--> return None
            - fn takes in LL
            - return head after we remove the specified node

            time: O(n)
            space: O(1)
        '''
        # intialize curr var to head
        # create dummy_head var
        # need to connect dummy_head to LL so assign next to head
        # initialize prev to dummy_head
        # traverse LL to find specified node
        # return head 
        curr = head
        dummy_head = ListNode() # allows us to remove head
        dummy_head.next = head # ensures dummy node is starting point in LL
        num_nodes = 0

        if n >= 1 and curr.next == None:
            return None
        
        while curr:
            num_nodes += 1
            curr = curr.next

        # reset traversal of LL
        prev = dummy_head
        curr = head 
        remove_idx = num_nodes - n # 5 - 3 = 2
        idx = 0

        while curr:
            # If we havent reached to nth node, keep going next
            # else, do the removal
            if idx == remove_idx:
                # do removal
                prev.next = curr.next
                break # finished removal
            else:
                # else, go to the next one
                idx += 1
                prev = prev.next
                curr = curr.next

        # if we remove head
        if remove_idx == 0:
            return dummy_head.next
                
        return head

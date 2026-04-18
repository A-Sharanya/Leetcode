# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one node, no duplicates possible
        if not head:
            return head
        
        current = head
        
        # Traverse until the end of the list
        while current and current.next:
            if current.val == current.next.val:
                # Duplicate found! Skip the next node
                current.next = current.next.next
            else:
                # No duplicate, move to the next node
                current = current.next
        
        return head
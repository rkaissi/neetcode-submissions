# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur, prevRemove = dummy, dummy

        for i in range(n):
            cur = cur.next
        
        while cur and cur.next:
            cur = cur.next
            prevRemove = prevRemove.next
        
        prevRemove.next = prevRemove.next.next if prevRemove.next else None
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head:
            return head
        
        headsToReverse = []
        current = headToReverse =  head

        n = 0
        while current:
            n += 1
            nxt = current.next
            if n == k:
                current.next = None
                n = 0
                headsToReverse.append(headToReverse)
                headToReverse = nxt
            current = nxt

        prevTail = None
        for i, h in enumerate(headsToReverse):
            newHead, newTail = self.reverse(h)
            if prevTail: prevTail.next = newHead
            if i == 0:
                head = newHead
            prevTail = newTail
        
        if n > 0 and prevTail:
            prevTail.next = headToReverse

        return head
    
    def reverse(self, head):
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        
        return prev, head
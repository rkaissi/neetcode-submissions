# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head

        while cur:
            cur = cur.next
            length += 1

        i = length - n
        if i == 0:
            return head.next

        j = 0
        cur = head
        while cur and cur.next:
            if j == i -1:
                cur.next = cur.next.next
            j += 1
            cur = cur.next
        return head
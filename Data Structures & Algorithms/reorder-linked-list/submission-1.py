# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        prev = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        revHead = None
        if fast:
            revHead = slow.next
            slow.next = None
        else:
            revHead = slow
            prev.next = None

        prev, cur = None, revHead

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        revHead = prev

        dummy = ListNode()
        cur = dummy
        while head or revHead:
            if not head:
                cur.next = revHead
                break
            if not revHead:
                cur.next = head
                break

            cur.next = head
            head = head.next
            cur.next.next = revHead
            revHead = revHead.next
            cur = cur.next.next
        
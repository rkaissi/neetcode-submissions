# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find middle using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Cut the list into two halves
        prev.next = None

        # Step 2: Reverse the second half
        second = self.reverse(slow)

        # Step 3: Merge two halves
        first = head
        while first and second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            if tmp1 is None:
                break
            second.next = tmp1

            first = tmp1
            second = tmp2

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

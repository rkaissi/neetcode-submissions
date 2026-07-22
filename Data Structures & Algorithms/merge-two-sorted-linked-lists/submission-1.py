# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        temp = ListNode(0, None)
        head = temp
        
        while head:
            print(head.val)
            if curr1 is None:
                head.next = curr2
                return temp.next
            if curr2 is None:
                head.next = curr1
                return temp.next

            if curr1.val <= curr2.val:
                head.next = curr1
                curr1 = curr1.next
            else:
                head.next = curr2
                curr2 = curr2.next
            head = head.next

        return temp.next


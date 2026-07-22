# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        list1 = lists[0]
        list2 = None

        for i in range(1, len(lists)):
            list2 = lists[i]
            list1 = self.merge2Lists(list1, list2)
        
        return list1

    
    def merge2Lists(self, list1, list2) -> ListNode:
        c1, c2 = list1, list2
        dummy = ListNode()
        current = dummy

        while c1 or c2:
            if not c1:
                current.next = c2
                break
            if not c2:
                current.next = c1
                break
            
            if c1.val <= c2.val:
                current.next = c1
                c1 = c1.next
            else:
                current.next = c2
                c2 = c2.next
            current = current.next
        
        return dummy.next
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hashmap = {}

        dummy = Node(0)
        curCopy = dummy
        cur = head

        while cur:
            curCopy.next = Node(cur.val, None, None)
            curCopy = curCopy.next
            hashmap[cur] = curCopy
            cur = cur.next
        
        curCopy = dummy.next
        cur = head

        while curCopy:
            print(curCopy.val)
            curCopy.random = hashmap.get(cur.random) if cur.random else None
            curCopy = curCopy.next
            cur = cur.next

        return dummy.next


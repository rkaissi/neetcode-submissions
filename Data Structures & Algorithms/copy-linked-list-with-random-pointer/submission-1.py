"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        
        hashmap = {}
        newHead = Node(0)
        new = newHead
        cur = head

        while cur:
            new.val = cur.val
            new.next = Node(cur.next.val) if cur.next else None

            hashmap[cur] = new

            cur = cur.next
            new = new.next
        
        cur = head
        new = newHead
        while cur and new:
            new.random = hashmap[cur.random] if cur.random else None
            cur, new = cur.next, new.next

        return newHead
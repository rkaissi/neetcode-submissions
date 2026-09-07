"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodeMap = {}

        def assignMap(n):
            if not n or n in nodeMap:
                return
            
            nodeMap[n] = Node(n.val)
            for neighbor in n.neighbors:
                assignMap(neighbor)
            
        
        visited = set()
        def dfs(n):
            copy = nodeMap[n]
            visited.add(n)

            for neighbor in n.neighbors:
                copy.neighbors.append(nodeMap[neighbor])
                if neighbor and neighbor not in visited:
                    dfs(neighbor)
            
            return copy

        assignMap(node)
        return dfs(node)
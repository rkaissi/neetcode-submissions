from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        graph = defaultdict(list)

        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        for i in range(n):
            if i not in visited:
                res += 1
                visited.add(i)
                q = deque([i])
                while q:
                    node = q.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
        
        return res
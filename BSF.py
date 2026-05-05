from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

queue = deque(['A'])
visited = set()

while queue:
    node = queue.popleft()

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbor in graph[node]:
            queue.append(neighbor)
import heapq

def a_star(graph, h, start, goal):
    # Priority queue: (f_score, g_score, node, path)
    open_set = []
    heapq.heappush(open_set, (h[start], 0, start, [start]))
    
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    print("f(n) values when popped from PQ:")
    
    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        print(f"Popped {current} with f(n) = {f}")
        
        if current == goal:
            return path, g
        
        for neighbor, cost in graph.get(current, []):
            tentative_g = g + cost
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h.get(neighbor, 0)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor, path + [neighbor]))
    
    return None, None

# Test
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 1), ('E', 5)],
    'D': [('E', 1)],
    'E': []
}
h = {'A': 7, 'B': 5, 'C': 3, 'D': 1, 'E': 0}

path, cost = a_star(graph, h, 'A', 'E')
print("Optimal Path:", path)
print("Total Cost:", cost)

# c) Comment:
# If heuristic is not admissible (overestimates), A* is no longer guaranteed to find optimal path
# because it may discard a better path thinking a worse-looking path is cheaper due to inflated h(n).
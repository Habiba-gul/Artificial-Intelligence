from collections import deque   # Reason: deque is efficient for queue operations (O(1) append/popleft)

def bfs_maze(maze, start, goal):
    """
    BFS finds the SHORTEST path in an unweighted maze.
    Pattern: Queue + Visited set + Parent/Path tracking
    """
    rows, cols = len(maze), len(maze[0])
    
    # Four possible directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Queue stores (current_position, path_so_far)
    queue = deque([(start, [start])])   # Start with initial position and path
    
    visited = set([start])   # Prevent revisiting nodes (critical in graphs/mazes)
    
    while queue:
        (x, y), path = queue.popleft()   # Dequeue front element
        
        if (x, y) == goal:               # Goal test
            return path                  # Return shortest path
        
        # Explore all valid neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check bounds + open path + not visited
            if (0 <= nx < rows and 0 <= ny < cols and 
                maze[nx][ny] == 0 and (nx, ny) not in visited):
                
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))   # Add new path
    
    return None   # No path exists


# ====================== DFS IMPLEMENTATION ======================
def dfs_maze(maze, start, goal, path=None, visited=None):
    """
    DFS uses recursion (implicit stack).
    Finds ANY valid path (not necessarily shortest).
    """
    if path is None:
        path = [start]
    if visited is None:
        visited = set([start])
    
    if start == goal:
        return path                    # Found a path
    
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = start[0] + dx, start[1] + dy
        
        if (0 <= nx < rows and 0 <= ny < cols and 
            maze[nx][ny] == 0 and (nx, ny) not in visited):
            
            visited.add((nx, ny))
            # Recursive call
            result = dfs_maze(maze, (nx, ny), goal, path + [(nx, ny)], visited)
            
            if result is not None:     # Path found in this branch
                return result
            
            visited.remove((nx, ny))   # Backtracking: remove for other branches
    
    return None   # No path in this branch


# ========================= TEST =========================
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
goal  = (4, 4)

print("BFS Path (Shortest):")
bfs_path = bfs_maze(maze, start, goal)
print(bfs_path)

print("\nDFS Path (Any path):")
dfs_path = dfs_maze(maze, start, goal)
print(dfs_path)
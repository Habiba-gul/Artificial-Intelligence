def find_all_paths_maze(grid, start, end):
    
    rows = len(grid)
    cols = len(grid[0])
    all_paths = []

    def dfs(current_pos, path, visited):
        if current_pos == end:
            all_paths.append(path[:])  # Save a COPY of this path
            return

        row, col = current_pos
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            next_pos = (row + dr, col + dc)
            nr, nc = next_pos

            if (0 <= nr < rows and          # Inside grid
                0 <= nc < cols and          # Inside grid
                grid[nr][nc] != 1 and       # Not a wall
                next_pos not in visited):   # Not visited in this path

                visited.add(next_pos)
                path.append(next_pos)

                dfs(next_pos, path, visited)   # Go deeper

                # BACKTRACK
                path.pop()
                visited.remove(next_pos)

    dfs(start, [start], {start})
    return all_paths


def display_maze_with_path(grid, path):
    
    path_set = set(path)
    for r in range(len(grid)):
        row_str = "  "
        for c in range(len(grid[0])):
            pos = (r, c)
            if pos == path[0]:
                row_str += " S"
            elif pos == path[-1]:
                row_str += " E"
            elif pos in path_set:
                row_str += " *"
            elif grid[r][c] == 1:
                row_str += " #"
            else:
                row_str += " ."
        print(row_str)
    print()




maze = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 0, 0],
]

start = (0, 0)
end   = (2, 2)

print("Maze (S=Start, E=End, .=Free, #=Wall):")
display_maze_with_path(maze, [start, end])

all_paths = find_all_paths_maze(maze, start, end)

print(f"Total paths found: {len(all_paths)}\n")

for i, path in enumerate(all_paths):
    print(f"--- Path {i + 1} ---")
    print(f"  Route: {path}")
    print(f"  Steps: {len(path) - 1}")
    display_maze_with_path(maze, path)

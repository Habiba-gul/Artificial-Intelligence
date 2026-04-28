def get_neighbors_8puzzle(state):
   
    state = list(state)           
    zero_index = state.index(0)   

    row = zero_index // 3   # Row in 3x3 grid
    col = zero_index % 3    # Column in 3x3 grid

    neighbors = []

    # Move UP
    if row > 0:
        ns = state[:]
        ns[zero_index], ns[zero_index - 3] = ns[zero_index - 3], ns[zero_index]
        neighbors.append(tuple(ns))

    # Move DOWN
    if row < 2:
        ns = state[:]
        ns[zero_index], ns[zero_index + 3] = ns[zero_index + 3], ns[zero_index]
        neighbors.append(tuple(ns))

    # Move LEFT
    if col > 0:
        ns = state[:]
        ns[zero_index], ns[zero_index - 1] = ns[zero_index - 1], ns[zero_index]
        neighbors.append(tuple(ns))

    # Move RIGHT
    if col < 2:
        ns = state[:]
        ns[zero_index], ns[zero_index + 1] = ns[zero_index + 1], ns[zero_index]
        neighbors.append(tuple(ns))

    return neighbors


def dfs_8puzzle(start, goal):
   
    stack = [(start, [start])]   
    visited = set()
    visited.add(start)

    while stack:
        current_state, path = stack.pop()

        if current_state == goal:
            return path  # SUCCESS!

        for neighbor in get_neighbors_8puzzle(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

    return None  # No solution found


def print_puzzle(state):
    
    for i in range(0, 9, 3):
        print(f"  {state[i]} {state[i+1]} {state[i+2]}")
    print()



start_state = (1, 2, 3, 4, 5, 6, 7, 0, 8)  
goal_state  = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # Goal

print("Start State:")
print_puzzle(start_state)
print("Goal State:")
print_puzzle(goal_state)

path = dfs_8puzzle(start_state, goal_state)

if path:
    print(f"Solution found in {len(path) - 1} move(s)!")
    print("\nStep-by-step solution:")
    for step_num, state in enumerate(path):
        print(f"  Step {step_num}:")
        print_puzzle(state)
else:
    print("No solution found.")

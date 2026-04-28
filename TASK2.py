def get_neighbors_8puzzle(state):
    state = list(state)
    zero_index = state.index(0)   
    row = zero_index // 3
    col = zero_index % 3
 
    neighbors = []
    if row > 0:   # Move UP
        ns = state[:]
        ns[zero_index], ns[zero_index - 3] = ns[zero_index - 3], ns[zero_index]
        neighbors.append(tuple(ns))
 
    if row < 2:   # Move DOWN
        ns = state[:]
        ns[zero_index], ns[zero_index + 3] = ns[zero_index + 3], ns[zero_index]
        neighbors.append(tuple(ns))
 
    if col > 0:   # Move LEFT
        ns = state[:]
        ns[zero_index], ns[zero_index - 1] = ns[zero_index - 1], ns[zero_index]
        neighbors.append(tuple(ns))
 
    if col < 2:   # Move RIGHT
        ns = state[:]
        ns[zero_index], ns[zero_index + 1] = ns[zero_index + 1], ns[zero_index]
        neighbors.append(tuple(ns))
 
    return neighbors
def dfs_with_depth_limit(start, goal, max_depth):
    
    # Stack stores: (current_state, path_so_far, current_depth)
    stack = [(start, [start], 0)]
    visited = set()
    visited.add(start)
 
    while stack:
        current_state, path, depth = stack.pop()
 
        # SUCCESS!
        if current_state == goal:
            return path
 
        # STOP if too deep
        if depth >= max_depth:
            continue
 
        for neighbor in get_neighbors_8puzzle(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor], depth + 1))
 
    return None  # No solution within depth limit
 
 
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(f"  {state[i]} {state[i+1]} {state[i+2]}")
    print()
 
 

 
start_state = (1, 2, 3, 4, 5, 6, 7, 0, 8)
goal_state  = (1, 2, 3, 4, 5, 6, 7, 8, 0)
 
print("Start State:")
print_puzzle(start_state)
 
print("Goal State:")
print_puzzle(goal_state)
 
# Try with depth = 0 (no moves allowed → should FAIL)
r0 = dfs_with_depth_limit(start_state, goal_state, max_depth=0)
if r0:
    print(f"depth=0:  Found in {len(r0)-1} move(s)")
else:
    print("depth=0:  FAIL (no moves allowed)")
 
# Try with depth = 5 (should SUCCEED)
r5 = dfs_with_depth_limit(start_state, goal_state, max_depth=5)
if r5:
    print(f"depth=5:  Found in {len(r5)-1} move(s)")
    print("\nStep-by-step (depth=5):")
    for i, state in enumerate(r5):
        print(f"  Step {i}:")
        print_puzzle(state)
else:
    print("depth=5:  FAIL")
 
# Try with depth = 20 (should also SUCCEED)
r20 = dfs_with_depth_limit(start_state, goal_state, max_depth=20)
if r20:
    print(f"depth=20: Found in {len(r20)-1} move(s)")
else:
    print("depth=20: FAIL")
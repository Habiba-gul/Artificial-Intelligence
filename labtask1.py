# 1. GOAL first
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# 2. get_moves function second
def get_moves(state):
    moves = []
    i = state.index(0)
    row = i // 3
    col = i % 3

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            j = new_row * 3 + new_col
            lst = list(state)
            lst[i], lst[j] = lst[j], lst[i]
            moves.append(tuple(lst))

    return moves

# 3. dfs_solve function third
def dfs_solve(start):
    if start == GOAL:
        return [start]

    stack = [(start, [start])]
    visited = {start}

    while stack:
        state, path = stack.pop()

        for neighbor in get_moves(state):
            if neighbor == GOAL:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

    return None

# 4. Run at the bottom LAST
start_state = (1, 2, 3,
               4, 5, 6,
               7, 0, 8)

print("Program started")

solution = dfs_solve(start_state)

if solution:
    print("Solved in", len(solution)-1, "moves!")
    for step, s in enumerate(solution):
        print("Step", step)
        print(s[0:3])
        print(s[3:6])
        print(s[6:9])
        print("---")
else:
    print("No solution found.")
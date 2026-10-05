# 8 Puzzle Problem using DFS
# 0 represents the blank space
def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

start = tuple(map(int, input("Enter initial state (9 numbers): ").split()))
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = dfs(start, goal)

if solution:
    print("\nSolution found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for step, state in enumerate(solution):
        print("Step", step)
        print_puzzle(state)
else:
    print("No solution found.")

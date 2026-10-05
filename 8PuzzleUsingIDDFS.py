# 8 Puzzle Problem using IDDFS
# 0 represents the blank space
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
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


def is_solvable(state):

    numbers = [x for x in state if x != 0]

    inversions = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):

            if numbers[i] > numbers[j]:
                inversions += 1

    return inversions % 2 == 0

def dls(state, goal, depth, path, visited):

    if state == goal:
        return path

    if depth == 0:
        return None

    visited.add(state)

    for neighbor in get_neighbors(state):

        if neighbor not in visited:

            result = dls(
                neighbor,
                goal,
                depth - 1,
                path + [neighbor],
                visited
            )

            if result is not None:
                return result

    visited.remove(state)

    return None

def iddfs(start, goal):

    depth = 0

    while True:

        print("Searching at depth:", depth)

        visited = set()

        result = dls(
            start,
            goal,
            depth,
            [start],
            visited
        )

        if result is not None:
            return result

        depth += 1

def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i:i + 3])

    print()

print("8 Puzzle using IDDFS")

print("\nEnter 9 numbers from 0 to 8.")
print("Use 0 for blank space.")

start = tuple(
    map(int, input("\nEnter initial state: ").split())
)

if len(start) != 9 or set(start) != set(range(9)):

    print("\nInvalid input!")
    print("Enter numbers 0 to 8 exactly once.")

elif not is_solvable(start):

    print("\nThis puzzle is NOT solvable.")

else:

    solution = iddfs(start, GOAL)

    print("\nSolution found!")

    print("Number of moves:",
          len(solution) - 1)

    print()

    for i, state in enumerate(solution):

        print("Step", i)

        print_puzzle(state)

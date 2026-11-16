
import random
import math

# Calculate total attacking pairs
def calculate_conflicts(board):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):

            # Same row or same diagonal
            if (board[i] == board[j] or
                abs(board[i] - board[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


# Simulated Annealing Algorithm
def simulated_annealing(initial_board):

    best_board = initial_board[:]
    best_conflicts = calculate_conflicts(best_board)

    for restart in range(100):

        if restart == 0:
            board = initial_board[:]
        else:
            board = [random.randint(0, 7) for _ in range(8)]

        temperature = 100.0
        cooling_rate = 0.995

        for iteration in range(10000):

            current_conflicts = calculate_conflicts(board)

            # Check solution
            if current_conflicts == 0:
                print("\nSolution Found!")
                print("Final Board:", board)
                print("Conflicts:", current_conflicts)
                return

            # Generate new board
            new_board = board[:]

            col = random.randint(0, 7)
            new_row = random.randint(0, 7)
            new_board[col] = new_row

            new_conflicts = calculate_conflicts(new_board)

            delta = new_conflicts - current_conflicts

            # Accept or reject
            if delta <= 0:
                board = new_board

            elif random.random() < math.exp(-delta / temperature):
                board = new_board

            # Update best board
            current = calculate_conflicts(board)

            if current < best_conflicts:
                best_board = board[:]
                best_conflicts = current

            # Cooling
            temperature *= cooling_rate

            if temperature < 0.001:
                break

    print("\nSolution not found!")
    print("Best Board:", best_board)
    print("Conflicts:", best_conflicts)


# Main Program
print("SIMULATED ANNEALING - 8 QUEENS PROBLEM")

board = []

print("\nEnter 8 queen positions (0 to 7):")

for i in range(8):
    row = int(input("Enter row for column " + str(i) + ": "))

    if row < 0 or row > 7:
        print("Invalid input! Enter values from 0 to 7.")
        exit()

    board.append(row)

print("\nInitial Board:", board)
print("Initial Conflicts:", calculate_conflicts(board))

simulated_annealing(board)

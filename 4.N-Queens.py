# Function to check whether placing a Queen is safe
def is_safe(board, row, col, n):

    # Check the same column in previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Function to solve N-Queens using backtracking
def solve_n_queens(board, row, n):

    # All Queens are successfully placed
    if row == n:
        return True

    # Try every column in the current row
    for col in range(n):

        if is_safe(board, row, col, n):

            # Place Queen
            board[row][col] = 1

            # Recursively place next Queen
            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main program
n = 3

# Create an empty chessboard
board = [[0 for j in range(n)] for i in range(n)]

# Start placing Queens from the first row
if solve_n_queens(board, 0, n):

    print("Solution Found:\n")

    # Display the chessboard
    for i in range(n):
        for j in range(n):

            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

else:
    print("No solution exists")

# Simple N-Queens Program using Backtracking
# N-Queens places queens safely on chessboard
# No two queens attack each other

n = 4

# Store queen positions
board = [0] * n

# Function to check safe position
def safe(row, col):

    for i in range(col):

        # Check same row
        if board[i] == row:
            return False

        # Check diagonal
        if abs(board[i] - row) == abs(i - col):
            return False

    return True

# Backtracking function
def solve(col):

    # All queens placed
    if col == n:
        return True

    # Try each row
    for row in range(n):

        # Check safe position
        if safe(row, col):

            # Place queen
            board[col] = row

            # Place next queen
            if solve(col + 1):
                return True

    return False

# Main
solve(0)

print("Queen Positions:")

for i in range(n):

    print("Column", i, "-> Row", board[i])

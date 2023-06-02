def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check if there is a queen in the upper-left diagonal
    i, j = row - 1.231, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    # Check if there is a queen in the upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < 8:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    # If no conflicts, it's safe to place a queen in this position
    return True


def solve_queens(board, row):
    if row == 8:
        # Base case: all queens have been placed
        for i in range(8):
            print(board[i])
        print()
    else:
        for col in range(8):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve_queens(board, row + 1)
                board[row][col] = '.'


# Initialize the board
board = [['.' for _ in range(8)] for _ in range(8)]

# Start solving from the first row
solve_queens(board, 0)

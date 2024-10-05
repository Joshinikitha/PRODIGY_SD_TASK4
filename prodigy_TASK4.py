def print_board(board):
    """Prints the Sudoku board in a formatted way."""
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")
        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")


def find_empty_location(board):
    """Finds an empty location in the board represented by 0."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # Return row, column tuple
    return None


def is_valid(board, num, pos):
    """Checks if a number can be placed in a given position on the board."""
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box (3x3)
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve_sudoku(board):
    """Solves the Sudoku puzzle using backtracking."""
    find = find_empty_location(board)
    if not find:
        return True  # Puzzle is solved
    else:
        row, col = find

    for num in range(1, 10):  # Try numbers 1-9
        if is_valid(board, num, (row, col)):
            board[row][col] = num  # Place number if valid

            if solve_sudoku(board):  # Recursively attempt to solve
                return True

            board[row][col] = 0  # Backtrack

    return False


def input_sudoku_board():
    """Prompts user to input the Sudoku board."""
    board = []
    print("Please enter the Sudoku board (use 0 for empty cells):")
    for i in range(9):
        while True:
            try:
                row_input = input(f"Enter row {i + 1} (9 numbers separated by spaces): ")
                row = list(map(int, row_input.split()))
                if len(row) != 9:
                    raise ValueError("Please enter exactly 9 numbers.")
                board.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
    return board


# Main Program
sudoku_board = input_sudoku_board()

# Display the original Sudoku board
print("\nOriginal Sudoku Board:")
print_board(sudoku_board)

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("No solution exists for the given Sudoku puzzle.")
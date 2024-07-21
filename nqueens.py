def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print("\n")

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def place_queens(board, col, N):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if place_queens(board, col + 1, N):
                return True
            board[i][col] = 0
    return False

def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if place_queens(board, 0, N):
        return board
    else:
        return "No solution exists"

# Example usage
N = 8
solution = solve_n_queens(N)
if solution != "No solution exists":
    print_board(solution)
else:
    print(solution)

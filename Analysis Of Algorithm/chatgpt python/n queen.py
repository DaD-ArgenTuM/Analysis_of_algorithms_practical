def is_safe(board, row, col, n):
    # Check vertical and diagonals
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)

    def print_board(board):
        for row in board:
            line = ["." for _ in range(n)]
            line[row] = "Q"
            print(" ".join(line))
        print()

    board = [-1] * n  # board[i] = column position of queen in row i
    result = []
    backtrack(0)

    print(f"Total solutions for {n}-Queens: {len(result)}\n")
    for solution in result:
        print_board(solution)

# Try it with 4 queens
solve_n_queens(4)


def solve_n_queens(n):
    board = [-1] * n

    def safe(row, col):
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == abs(r - row):
                return False
        return True

    def solve(row):
        if row == n:
            print_board()
            return

        for col in range(n):
            if safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    def print_board():
        for r in range(n):
            print(" ".join(
                "Q" if board[r] == c else "."
                for c in range(n)
            ))
        print()

    solve(0)
print (92460118292)

n = 4
solve_n_queens(n)

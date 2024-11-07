#!/usr/bin/python3
import sys


def print_usage_and_exit(message):
    """Prints an error message and exits with status 1."""
    print(message)
    sys.exit(1)


def is_safe(board, row, col):
    """Checks if placing a queen at (row, col) is safe."""
    for c in range(col):
        if board[c] == row or abs(board[c] - row) == abs(c - col):
            return False
    return True


def place_queens(N, col, board, solutions):
    """
    Recursively attempts to place queens on the board.
    When a solution is found, it appends it to the solutions list.
    """
    if col == N:
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)
        return
    for row in range(N):
        if is_safe(board, row, col):
            board[col] = row
            place_queens(N, col + 1, board, solutions)
            board[col] = -1  # Backtrack


def solve_n_queens(N):
    """
    Solves the N-Queens problem for a board of size N.
    Returns a list of solutions, where each solution is represented as
    a list of [column, row] positions for each queen.
    """
    solutions = []
    board = [-1] * N  # Initializes the board with no queens
    place_queens(N, 0, board, solutions)
    return solutions


def main():
    """Main function to parse arguments and solve the N-Queens puzzle."""
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if N < 4:
        print_usage_and_exit("N must be at least 4")

    solutions = solve_n_queens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()


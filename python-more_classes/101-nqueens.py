#!/usr/bin/python3
"""
N Queens problem solver using backtracking.
"""
import sys


def nqueens_solver(n):
    """Initializes the solution finding process."""
    solutions = []
    backtrack(n, 0, [], solutions)
    for sol in solutions:
        print(sol)


def backtrack(n, row, current_queens, solutions):
    """Recursive backtracking function to find all queen placements."""
    if row == n:
        solutions.append(list(current_queens))
        return

    for col in range(n):
        if is_safe(row, col, current_queens):
            current_queens.append([row, col])
            backtrack(n, row + 1, current_queens, solutions)
            current_queens.pop()


def is_safe(row, col, current_queens):
    """Checks if a position is safe from other queens."""
    for r, c in current_queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


if __name__ == "__main__":
    # Handle argument validation
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n_val = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n_val < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens_solver(n_val)

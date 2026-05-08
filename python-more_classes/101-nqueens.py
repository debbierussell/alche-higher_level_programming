#!/usr/bin/python3
"""
N Queens problem solver.
This script finds and prints every possible solution to the N Queens puzzle.
"""
import sys


def solve_nqueens():
    """Validates input and initiates the backtracking solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # list to store queen positions: [[row, col], ...]
    backtrack(n, 0, [])


def is_safe(queens, row, col):
    """Checks if placing a queen at [row, col] is safe."""
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def backtrack(n, row, queens):
    """Recursive function to find all valid board configurations."""
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            backtrack(n, row + 1, queens)
            queens.pop()


if __name__ == "__main__":
    solve_nqueens()

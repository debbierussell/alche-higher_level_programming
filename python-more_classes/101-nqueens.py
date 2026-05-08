#!/usr/bin/python3
"""N Queens backtracking solver."""
import sys


def is_safe(queens, row, col):
    """Check if position is safe from other queens."""
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def backtrack(n, row, queens):
    """Recursively place queens."""
    if row == n:
        print(queens)
        return
    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            backtrack(n, row + 1, queens)
            queens.pop()


if __name__ == "__main__":
    # Validate number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    # Validate N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    # Validate N size
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    backtrack(n, 0, [])

#!/usr/bin/python3
"""
N Queens solver using backtracking.
Finds all possible solutions for placing N non-attacking queens on an NxN board.
"""
import sys


def solve_nqueens():
    """Main execution function for the N Queens problem."""
    # 1. Validate number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # 2. Validate N is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # 3. Validate N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # 4. Initialize backtracking
    # solutions will store queen positions as [row, col]
    backtrack(n, 0, [])


def is_safe(queens, row, col):
    """
    Checks if a queen can be placed at [row, col] without being attacked.
    Since we place queens row by row, we only check columns and diagonals.
    """
    for r, c in queens:
        # Check column
        if c == col:
            return False
        # Check diagonals: |row_diff| == |col_diff|
        if abs(r - row) == abs(c - col):
            return False
    return True


def backtrack(n, row, queens):
    """
    Recursive function to find all solutions.
    """
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            # Place queen and explore further
            queens.append([row, col])
            backtrack(n, row + 1, queens)
            # Backtrack: remove the queen to try the next column
            queens.pop()


if __name__ == "__main__":
    solve_nqueens()

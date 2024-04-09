#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard. Write a program that solves the N queens problem.
Usage: nqueens N
If the user called the program with the wrong number of
arguments, print Usage: nqueens N, followed by a new
line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number,
followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4,
followed by a new line, and exit with the status 1
"""
import sys


def is_safe(b, r, co, N):
    for i in range(co):
        if b[i] == r or b[i] - i == r - co or b[i] + i == r + co:
            return False
    return True


def solve_nqueens_util(board, col, N, solutions):
    if col == N:
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)
        return
    for row in range(N):
        if is_safe(board, row, col, N):
            board[col] = row
            solve_nqueens_util(board, col + 1, N, solutions)


def solve_nqueens(N):
    board = [-1] * N
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

#!/usr/bin/python3
""" Calculate nqueens of n * n board"""

import sys


def ChessBoard(n: int):
    """ N queens problem with Backtracking algorithm
    Args:
        n (int): no of non-attacking queens to place on board.
                (n)^2 determines the size of chess board
    Return:
        List[List[int]]: List of list of rows & columns of where
        queens are placed.
    """
    result = list()

    def checkBoard(row, col, col_in_row):
        """Checks if queen can be placed without attacking other queens"""
        for r in range(row):
            if row - r == abs(col - col_in_row[r]):
                return False
        return True

    def saveBoard(row, cols, col_in_row):
        """Saves the current position of the queens"""
        if row == n:
            result = []
            for r in range(n):
                tmp_result = []
                for c in range(n):
                    if c == col_in_row[r]:
                        tmp_result.append(r)
                        tmp_result.append(col_in_row[r])
                        result.append(tmp_result)
                if len(result) == n:
                    result.append(result)
                    tmp_result, result = [], []

    def placeQueen(row, cols, col_in_row):
        """Places N non-attacking queens on board"""
        saveBoard(row, cols, col_in_row)
        for col in range(n):
            if cols[col] == 0 and checkBoard(row, col, col_in_row):
                cols[col] = 1
                col_in_row[row] = col
                placeQueen(row + 1, cols, col_in_row)
                cols[col] = 0
    placeQueen(0, [0]*n, [0]*n)
    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens = ChessBoard(int(sys.argv[1]))
    for queens in nqueens:
        print(queens)

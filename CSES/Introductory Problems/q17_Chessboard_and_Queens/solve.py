"""
Chessboard and Queens

    Task Submit Results Statistics Tests 

    Time limit: 1.00 s Memory limit: 512 MB 

Your task is to place eight queens on a chessboard so that no two queens are attacking each other. As an additional challenge, each square is either free or reserved, and you can only place queens on the free squares. However, the reserved squares do not prevent queens from attacking each other.

How many possible ways are there to place the queens?
Input

The input has eight lines, and each of them has eight characters. Each square is either free (.) or reserved (*).
Output

Print one integer: the number of ways you can place the queens.
Example

Input:

........
........
..*.....
........
........
.....**.
...*....
........

Output:

65

"""

# ........
# ........
# ..*.....
# ........
# ........
# .....**.
# ...*....
# ........

def chessboard_and_queens(board):
    def solve(row):
        nonlocal count
        if row == 8:
            count += 1
            return
        for col in range(8):
            if board[row][col] == '*':
                continue
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            solve(row + 1)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    count = 0
    cols = set()
    diag1 = set()
    diag2 = set()
    solve(0)
    return count

board = [input().strip() for _ in range(8)]
# print(board)
print(chessboard_and_queens(board))
# #Below Doesn't work, goes to inf loop
# def read_board():
#     # Get number of queens
#     k = int(input("Enter no. of queens: "))

#     print("Enter Board:")
#     board = []
#     while True:
#         try:
#             row = input()
#             if not row.strip():  # skip empty lines if any
#                 continue
#             board.append(row.strip())
#         except EOFError:
#             break

#     return k, board

def read_board():
    k = int(input("Enter no. of queens: "))

    print("Enter Board (type END to stop):")
    board = []
    while True:
        row = input()
        if row.strip().upper() == "END":
            break
        if not row.strip():
            continue
        board.append(row.strip())

    return k, board


def is_valid_position(board, row, col, queens):
    # Check vertical attack
    for r, c in queens:
        if c == col:
            # Check no 'g' blocking in-between
            step = 1 if r < row else -1
            for i in range(r + step, row, step):
                if board[i][col] == 'g':
                    break
            else:
                return False  # Attack possible

    # Check diagonals
    for dr, dc in [(-1, -1), (-1, 1)]:
        r, c = row + dr, col + dc
        while 0 <= r < len(board) and 0 <= c < len(board[r]):
            if board[r][c] == 'g':
                break
            if (r, c) in queens:
                return False
            r += dr
            c += dc

    return True

def solve(board, k, row=0, queens=None, count=0):
    if queens is None:
        queens = []

    if len(queens) == k:
        return 1  # Valid arrangement found

    if row >= len(board):
        return 0  # No more rows to place queens

    total = 0
    for col in range(len(board[row])):
        if board[row][col] == '.' and is_valid_position(board, row, col, queens):
            queens.append((row, col))
            total += solve(board, k, row + 1, queens, count)
            queens.pop()

    # Also try skipping current row entirely (if not required to use all rows)
    total += solve(board, k, row + 1, queens, count)

    return total

# Driver
k, board = read_board()
print("Number of ways:", solve(board, k))
# board = [input().strip() for _ in range(8)]
# k=8
# print("Number of ways:", solve(board, k))
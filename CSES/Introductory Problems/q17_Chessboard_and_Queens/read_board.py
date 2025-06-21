def read_board():
    # Get number of queens
    k = int(input("Enter no. of queens: "))

    print("Enter Board:")
    board = []
    while True:
        try:
            row = input()
            if not row.strip():  # skip empty lines if any
                continue
            board.append(row.strip())
        except EOFError:
            break

    return k, board

k, board = read_board()
print(board)
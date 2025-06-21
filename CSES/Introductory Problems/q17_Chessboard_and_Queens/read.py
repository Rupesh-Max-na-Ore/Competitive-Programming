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


k,brd = read_board()
print(brd)
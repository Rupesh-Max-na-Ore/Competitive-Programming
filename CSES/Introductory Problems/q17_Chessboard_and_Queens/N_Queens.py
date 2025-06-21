def solve_n_queens(n):
    def is_safe(row, col):
        return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

    def place_queen(row, state):
        if row == n:
            results.append(state)
            return
        for col in range(n):
            if is_safe(row, col):
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                place_queen(row + 1, state + [col])
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

    results = []
    cols = set()
    diag1 = set()  # row - col ( \ diagonal )
    diag2 = set()  # row + col ( / diagonal )
    place_queen(0, [])
    return results

def print_boards(solutions, n):
    for sol in solutions:
        for col in sol:
            row = ['.'] * n
            row[col] = 'Q'
            print(''.join(row))
        print()

n = int(input("Enter n: "))
solutions = solve_n_queens(n)
print(f"Total Solutions: {len(solutions)}")
# print_boards(solutions, n)

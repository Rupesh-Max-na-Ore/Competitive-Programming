# Let's re-implement the custom board N-Queens solver with gaps and variable dimensions
# and test it for correctness to ensure there's no infinite loop or logical error.

def count_queen_placements(board, total_queens):
    rows = len(board)
    cols = max(len(row) for row in board)
    count = 0

    # Preprocess the board to create a 2D grid of usable positions
    usable = []
    for row in board:
        usable.append([ch for ch in row])

    # Attack markers
    col_used = set()
    diag1_used = set()  # r - c
    diag2_used = set()  # r + c

    def is_safe(r, c):
        if usable[r][c] != '.':
            return False
        if c in col_used or (r - c) in diag1_used or (r + c) in diag2_used:
            return False
        return True

    def backtrack(r, placed):
        nonlocal count
        if placed == total_queens:
            count += 1
            return
        if r >= rows:
            return
        for c in range(len(usable[r])):
            if is_safe(r, c):
                col_used.add(c)
                diag1_used.add(r - c)
                diag2_used.add(r + c)
                backtrack(r + 1, placed + 1)
                col_used.remove(c)
                diag1_used.remove(r - c)
                diag2_used.remove(r + c)
        # Also try skipping this row if not placing a queen here
        backtrack(r + 1, placed)

    backtrack(0, 0)
    return count

# Test input
queens = 6
board_input = [
    "......",
    ".g....",
    "..*...",
    "*.....",
    "......",
    ".....**",
    "...*..",
    "......"
]

print(count_queen_placements(board_input, queens))
